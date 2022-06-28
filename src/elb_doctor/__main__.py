from __future__ import print_function, unicode_literals
from elb_easy.lib.getElbs import getElbs, getElbsV2
from elb_easy.lib.parseElbs import parseElbs
from elb_easy.lib.describeHealth import getTargetHealth
from elb_easy.lib.tgs.tgHandler import tgHandler
from elb_easy.lib.healthHandler import processHealth
from elb_easy.lib.utilities import healthbar,bcolors
from PyInquirer import prompt
from elb_easy.lib.regions import standard_regions,other_regions
from elb_easy.lib.elbtypes import elb_types
import time

def main():

    #Question 1: Region OR Auto detection feature 
    #Question 2: ELB Type 
    #Question 3: ELB ARN/name
    #(optional): TG ARN 

    questions = [
        {
        'type': 'list',
        'name': 'standard_regions',
        'message': 'What is the AWS region of your ELB?',
        'choices': standard_regions,
        'default': 'us-east-1'
        },
        {
        'type': 'list',
        'name': 'other_regions',
        'message': 'Is your ELB in any of the following Opt-in/GovCloud/China region?',
        'choices': other_regions,
        'when': lambda answers: answers['standard_regions'] == False
        },
        {
            'type': 'list',
            'name': 'elb_type',
            'message': 'What is the type of your ELB?',
            'choices': elb_types
        },
        {
            'type': 'list',
            'name': 'elb',
            'message': 'Which CLB are you having issue with?',
            'choices': parseElbs(getElbs()),
            'when': lambda answers: answers['elb_type'] == 'classic'
        },
        {
            'type': 'list',
            'name': 'elb',
            'message': 'Which ALB are you having issue with?',
            'choices': parseElbs(getElbsV2()),
            'when': lambda answers: answers['elb_type'] != 'classic'
        },
        {
            'type': 'list',
            'name': 'tg',
            'message': 'Which TG/backend are you having issue with?',
            'choices': tgHandler,                                    #this is always invoked despite if the question is asked, causing problem when CLB is selected
            'when': lambda answers: answers['elb_type'] != 'classic'
        }
    ]

    answers = prompt(questions)
    outputs = getTargetHealth(answers)
    # print(outputs)
    HealthyHostCount,UnHealthyHostCount = processHealth(answers,outputs)

    print("\n")

    if answers['elb_type'] == 'classic':
        for i in healthbar(range(len(outputs["InstanceStates"])),HealthyHostCount, "  Healthy Targets: ", 100):
            time.sleep(0.03) # any code you need

        print(bcolors.FAIL)
        for i in healthbar(range(len(outputs["InstanceStates"])),UnHealthyHostCount, "Unhealthy Targets: ", 100):
            time.sleep(0.03) # any code you need
        print(bcolors.ENDC)

        row_format ="{:<30}{:<30}{:<40}{:<40}"
        print(row_format.format('Target:Port','HealthState','Reason','Description'))
        for i in outputs["InstanceStates"]:
            if i["State"] == "OutOfService":
                print(row_format.format(i["InstanceId"],bcolors.FAIL+i["State"]+bcolors.ENDC,i["ReasonCode"],i["Description"]))
            else: 
                print(row_format.format(i["InstanceId"],bcolors.OKGREEN+i["State"]+bcolors.ENDC,i["ReasonCode"],i["Description"]))

    elif answers['elb_type'] != 'classic':
        
        for i in healthbar(range(len(outputs["TargetHealthDescriptions"])),HealthyHostCount, "  Healthy Targets: ", 100):
            time.sleep(0.03) # any code you need

        print(bcolors.FAIL)
        for i in healthbar(range(len(outputs["TargetHealthDescriptions"])),UnHealthyHostCount, "Unhealthy Targets: ", 100):
            time.sleep(0.03) # any code you need
        print(bcolors.ENDC)

        row_format ="{:<30}{:<30}{:<40}{:<40}"
        print(row_format.format('Target:Port','HealthState','Reason','Description'))
        for i in outputs["TargetHealthDescriptions"]:
            if i["TargetHealth"]["State"] == "unhealthy":
                print(row_format.format(i["Target"]["Id"]+":"+str(i["Target"]["Port"]),bcolors.FAIL+i["TargetHealth"]["State"]+bcolors.ENDC,i["TargetHealth"]["Reason"],i["TargetHealth"]["Description"]))
            else: 
                print(row_format.format(i["Target"]["Id"]+":"+str(i["Target"]["Port"]),bcolors.OKGREEN+i["TargetHealth"]["State"]+bcolors.ENDC,"",""))

if __name__ == "__main__":
    main()
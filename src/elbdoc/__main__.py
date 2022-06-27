from __future__ import print_function, unicode_literals
from elb_easy.lib.getElbs import getElbs, getElbsV2
from elb_easy.lib.parseElbs import parseElbs
from elb_easy.lib.describeHealth import getTargetHealth
from elb_easy.lib.tgs.getTg import getTG
from elb_easy.lib.utilities import healthbar,bcolors
from PyInquirer import prompt
from elb_easy.lib.regions import standard_regions,other_regions
from elb_easy.lib.elbtypes import elb_types
import time   

def main():

    #Question 1: Region or Auto detection feature 
    #Question 2: ELB Type 
    #Question 3: ELB ARN  
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
        }
    ]

    answers = prompt(questions)

    if (answers["elb_type"]=="classic"): 
        output = parseElbs(getElbs())
        choices = [] 
        for name,arn in output.items(): 
            choices.append({
                'name': name,
                'value': arn 
            })
    else:                                #it's currently returning all ALB, NLB and GWLB
        output = parseElbs(getElbsV2())
        choices = [] 
        for name,arn in output.items(): 
            choices.append({
                'name': name,
                'value': arn 
            })

    questions = [
        {
            'type': 'list',
            'name': 'ALB',
            'message': 'Which ALB are you having issue with?',
            'choices': choices
        }
    ]

    answers = prompt(questions)

    outputs = (getTG(answers["ALB"]))

    choices.clear()

    for i in outputs['TargetGroups']:
        choices.append({
            'name': i["TargetGroupName"],
            'value': i["TargetGroupArn"]
        })

    questions = [
        {
            'type': 'list',
            'name': 'TargetGroup',
            'message': 'Which TG/backend are you having issue with?',
            'choices': choices
        }
    ]

    answers = prompt(questions)
    outputs = getTargetHealth(answers["TargetGroup"])

    #option 1: count the outputs 
    #option 2: get it from CW metrics


    UnHealthyHostCount=0
    HealthyHostCount=0
    for i in outputs["TargetHealthDescriptions"]:
        if i["TargetHealth"]["State"] == "unhealthy":
            UnHealthyHostCount+=1 
            
        elif i["TargetHealth"]["State"] == "healthy":
            HealthyHostCount+=1
    print("\n")
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

if __name__ == "__main__":
    main()
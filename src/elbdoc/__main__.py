from __future__ import print_function, unicode_literals
from elb_easy.lib.getElbs import getElbs
from elb_easy.lib.parseElbs import parseElbs
from elb_easy.lib.describeHealth import getTargetHealth
from elb_easy.lib.tgs.getTg import getTG
from elb_easy.lib.utilities import healthbar,bcolors
from PyInquirer import prompt
import time   

def main():
    questions = [
        {
            'type': 'list',
            'name': 'ElbType',
            'message': 'What is the type of ELB?',
            'choices': [
                {
                    'key': 'p',
                    'name': 'CLB',
                    'value': 'all-elb'
                },
                {
                    'key': 'a',
                    'name': 'ALB',
                    'value': 'get-alb'
                },
                {
                    'key': 'w',
                    'name': 'NLB',
                    'value': 'get-nlb'
                }
            ]
        }

        #needs to check region as well?
    ]

    answers = prompt(questions)
    if (answers["ElbType"]=="get-alb"): 
        output = parseElbs(getElbs())        #getElbs currently return all ELBs 
        # print(type(output))
        choices = [] 
        for key,value in output.items(): 
            # print(key+"xxxx"+value)
            choices.append({
                'name': key,
                'value': value 
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
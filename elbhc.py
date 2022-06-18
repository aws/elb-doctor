from __future__ import print_function, unicode_literals
from elb_easy.lib.getElbs import getElbs
from elb_easy.lib.parseElbs import parseElbs
from elb_easy.lib.describeHealth import getTargetHealth
from elb_easy.lib.tgs.getTg import getTG
from PyInquirer import prompt
import pprint as pp 

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

    #needs to check region as well?????
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

# print (answers)
outputs = (getTG(answers["ALB"]))

choices.clear()
# print(type(outputs["TargetGroups"]))
for i in outputs['TargetGroups']:
    choices.append({
        'name': i["TargetGroupName"],
        'value': i["TargetGroupArn"]
    })

# print(choices)

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
pp.pprint(outputs["TargetHealthDescriptions"])
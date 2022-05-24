from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import boto3
import json

questions = [
    {
        'type': 'input',
        'name': 'tgArn',
        'message': 'What\'s the ARN of your target group?',
    },
    {
        'type': 'confirm',
        'name': 'onGoing',
        'message': 'Is the event onging?',
        'default': False
    },
    {
        'type': 'list',
        'name': 'httpError',
        'message': 'What is the HTTP status code?',
        'choices': [
            {
                'key': 'p',
                'name': 'HTTP 502',
                'value': '502'
            },
            {
                'key': 'a',
                'name': 'HTTP 503',
                'value': '503'
            },
            {
                'key': 'w',
                'name': 'HTTP 504',
                'value': '504'
            }
        ]
    }
]

answers = prompt(questions)

# print(answers)  
s3 = boto3.resource('s3')
client = boto3.client('elbv2')

response = client.describe_target_health(
    TargetGroupArn='arn:aws:elasticloadbalancing:ap-southeast-2:318360445202:targetgroup/onos-alb-0-instance-tg-0/225950b0e96972dd',
    Targets=[
        {
            'Id': 'i-02b8769a50bc64b1a',
            'Port': 8801
        },
    ]
)

print(json.dumps(response["TargetHealthDescriptions"],indent=4))


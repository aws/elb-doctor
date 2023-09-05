from __future__ import print_function, unicode_literals
from elb_doctor.lib.elb.get_elbs import GetElbs
from elb_doctor.lib.elb.parse_elbs import ParseElbs
from elb_doctor.lib.tgs.getTargetHealth import getTargetHealth
from elb_doctor.lib.tgs.parseTgHealth import parseTgHealth
from elb_doctor.lib.helpers.utilities import output_renderer
from PyInquirer import prompt
from elb_doctor.lib.helpers.regions import standard_regions,other_regions
from elb_doctor.lib.helpers.elbtypes import elb_types
from elb_doctor.api.elb_doctor_api import ElbDoctorApi

[default]
aws_access_key_id = AKIA2OGYBAH63YITYPN4
aws_secret_access_key = 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
output = json
region = us-east-1
[default]
aws_access_key_id = AKIA2OGYBAH63YITYPN4
aws_secret_access_key = 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
output = json
region = us-east-1

mongodb+srv://my-user:my-password@clustername.mongodb.net/

asic auth:

https://admin:admin@the-internet.herokuapp.com/basic_auth

Private key:
-----BEGIN OPENSSH PRIVATE KEY-----
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
Hx7UPVlTK8dyvk1Z+Yw0nrfNClI=
-----END OPENSSH PRIVATE KEY-----

def main():

    # get_elb = GetElbs()
    api = ElbDoctorApi()
    # parse_elbs = ParseElbs()

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
            'choices': api.retrieve_clbs,
            'when': lambda answers: answers['elb_type'] == 'classic'
        },
        {
            'type': 'list',
            'name': 'elb',
            'message': 'Which ALB are you having issue with?',
            'choices': api.retrieve_elbv2,                   #currently there is no better way to call parse_elbs.parse_albs, parse_elbs.parse_nlbs or parse_elbs.parse_gwlbs other than duplicating this question 3 times and use 'when' to control which one to display. get_elbv2 call will also be duplicated as well.
            'when': lambda answers: answers['elb_type'] == 'application'
        },
        {
            'type': 'list',
            'name': 'elb',
            'message': 'Which NLB are you having issue with?',
            'choices': api.retrieve_elbv2,                   #currently there is no better way to call parse_elbs.parse_albs, parse_elbs.parse_nlbs or parse_elbs.parse_gwlbs other than duplicating this question 3 times and use 'when' to control which one to display. get_elbv2 call will also be duplicated as well.
            'when': lambda answers: answers['elb_type'] == 'network'
        },
        {
            'type': 'list',
            'name': 'elb',
            'message': 'Which GWLB are you having issue with?',
            'choices': api.retrieve_elbv2,                   #currently there is no better way to call parse_elbs.parse_albs, parse_elbs.parse_nlbs or parse_elbs.parse_gwlbs other than duplicating this question 3 times and use 'when' to control which one to display. get_elbv2 call will also be duplicated as well.
            'when': lambda answers: answers['elb_type'] == 'gateway'
        },
        {
            'type': 'list',
            'name': 'tg',
            'message': 'Which TG/backend are you having issue with?',
            'choices': api.retrieve_target_groups,                                   #this is always invoked despite if the question is asked, causing problem when CLB is selected
            'when': lambda answers: answers['elb_type'] != 'classic'
        }
    ]
    
    answers = prompt(questions)
    targets_health,tg_target_count = getTargetHealth(answers)
    healthy_host_count,unhealthy_host_count = parseTgHealth(answers,targets_health)  #consider to fetch from CW metrics, easier for AZ specific data
    
    print("\n")

    renderer = output_renderer()
    if answers['elb_type'] == 'classic':
        renderer.output_v1(targets_health,healthy_host_count,unhealthy_host_count)
    elif answers['elb_type'] != 'classic':
        renderer.output_v2(answers,targets_health,healthy_host_count,unhealthy_host_count,tg_target_count)

if __name__ == "__main__":
    main()

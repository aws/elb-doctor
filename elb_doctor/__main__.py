# from __future__ import print_function, unicode_literals
# from elb_doctor.elb.getElbs import getElbs, getElbsV2
# from elb_doctor.elb.parseElbs import parseElbs
# from elb_doctor.tgs.getTargetHealth import getTargetHealth
# from elb_doctor.tgs.tgHandler import tgHandler
# from elb_doctor.tgs.parseTgHealth import parseTgHealth
# from elb_doctor.helpers.utilities import output_renderer
# from PyInquirer import prompt
# from elb_doctor.helpers.regions import standard_regions,other_regions
# from elb_doctor.helpers.elbtypes import elb_types

from __future__ import print_function, unicode_literals
from elb.getElbs import getElbs, getElbsV2
from elb.parseElbs import parseElbs
from tgs.getTargetHealth import getTargetHealth
from tgs.tgHandler import tgHandler
from tgs.parseTgHealth import parseTgHealth
from helpers.utilities import output_renderer
from PyInquirer import prompt
from helpers.regions import standard_regions,other_regions
from helpers.elbtypes import elb_types


def main():

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
            'choices': tgHandler,                                         #this is always invoked despite if the question is asked, causing problem when CLB is selected
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

from secrets import choice
from tgs.getTg import getTG
from PyInquirer import Separator

def tgHandler(answers) -> list:

    if(answers['elb_type'] == 'classic'): return    #prevent invocation if CLB is selected
        
    choices = []
    outputs = getTG(answers)

    for i in outputs['TargetGroups']:
        if 'Matcher' in i: 
            choices.append({
                'name': i['TargetGroupName'],
                'value': {
                    'tg_arn': i['TargetGroupArn'],
                    'success_codes': i['Matcher']['HttpCode'],
                    'hc_timeout': i['HealthCheckTimeoutSeconds']
                }
            })
        else: 
            choices.append({
                'name': i['TargetGroupName'],
                'value': {
                    'tg_arn': i["TargetGroupArn"],
                    'hc_timeout': i['HealthCheckTimeoutSeconds']
                }
            })
    
    choices.append(Separator())
    choices.append({
        'name': 'all target groups',
        'value': {
            'tg_arn': 'all_tg',
            'tgs': choices
        }
    })

    return choices



 
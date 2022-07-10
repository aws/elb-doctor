
from secrets import choice
from tgs.getTg import getTG
from PyInquirer import Separator

def tgHandler(answers) -> list:

    if(answers['elb_type'] == 'classic'): return    #prevent invocation if CLB is selected
        
    choices = []
    all_tgs = []
    outputs = getTG(answers)

    for i in outputs['TargetGroups']:
        if 'Matcher' in i: 
            choices.append({
                'name': i['TargetGroupName'],
                'value': [
                    {
                    'tg_arn': i['TargetGroupArn'],
                    'success_codes': i['Matcher']['HttpCode'],
                    'hc_timeout': i['HealthCheckTimeoutSeconds']
                    }
                ]
            })
            all_tgs.append(choices[-1]['value'][0])
        else: 
            choices.append({
                'name': i['TargetGroupName'],
                'value': [
                    {
                    'tg_arn': i["TargetGroupArn"],
                    'hc_timeout': i['HealthCheckTimeoutSeconds']
                    }
                ] 
            })
            all_tgs.append(choices[-1]['value'][0])
    
    choices.append(Separator())
    choices.append({
        'name': 'all target groups',
        'value': all_tgs
    })

    # print(choices)
    # print(all_tgs)
    
    return choices



 
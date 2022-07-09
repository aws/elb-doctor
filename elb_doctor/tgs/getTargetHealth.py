from typing import Dict
import boto3

def getTargetHealth(answers) -> Dict:
    """Retrieves all target status in this Target Group"""

    if answers['tg']['tg_arn'] == 'all_tg':
        client = boto3.client('elbv2')
        for i in range(0,len(answers['tg']['tgs'])-2):     #answers['tg']['tgs'] has a 'Separator' object and 'all target groups' option in the end, therefore excluding the last 2 options. 
            if 'response' not in locals(): 
                response = client.describe_target_health(TargetGroupArn=answers['tg']['tgs'][i]['value']['tg_arn']) 
            else:
                temp = client.describe_target_health(TargetGroupArn=answers['tg']['tgs'][i]['value']['tg_arn'])
                response['TargetHealthDescriptions'] = response['TargetHealthDescriptions']+temp['TargetHealthDescriptions']
        return response

    if answers['elb_type'] == 'classic':
        client = boto3.client('elb')
        response = client.describe_instance_health(LoadBalancerName=answers['elb'])

    elif answers['elb_type'] != 'classic':
        client = boto3.client('elbv2')
        response = client.describe_target_health(TargetGroupArn=answers['tg']['tg_arn'])

    return response
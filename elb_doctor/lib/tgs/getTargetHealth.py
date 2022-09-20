from re import T
from typing import Dict
import boto3

def getTargetHealth(answers) -> Dict:
    """Retrieves all target status in this Target Group"""

    tg_target_count = []   #for all tg   ---> won't work if need to filter healthy targets
    if answers['elb_type'] == 'classic':

        client = boto3.client('elb')
        response = client.describe_instance_health(LoadBalancerName=answers['elb'])
        return response,tg_target_count

    else: 
        client = boto3.client('elbv2')
        for i in answers['tg']:
            if 'response' not in locals(): 
                response = client.describe_target_health(TargetGroupArn=i['tg_arn'])
                tg_target_count.append(len(response['TargetHealthDescriptions']))
            else:
                temp = client.describe_target_health(TargetGroupArn=i['tg_arn'])
                tg_target_count.append(len(temp['TargetHealthDescriptions']))
                response['TargetHealthDescriptions'] = response['TargetHealthDescriptions']+temp['TargetHealthDescriptions']

        return response,tg_target_count
        
"""
{
    'TargetHealthDescriptions': [
                                {tg1-target1},{tg1-target2},
                                {tg2-target1},
                                {tg3-target1},{tg3-target2},{tg3-target3}
                                ],
    'ResponseMetadata': {...}
}
"""

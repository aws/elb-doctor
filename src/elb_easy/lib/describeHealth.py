from typing import Dict
import boto3

def getTargetHealth(answers) -> Dict:
    """Retrieves all target status in this Target Group"""

    if answers['elb_type'] == 'classic':
        client = boto3.client('elb')
        response = client.describe_instance_health(LoadBalancerName=answers['elb'])

    elif answers['elb_type'] != 'classic':
        client = boto3.client('elbv2')
        response = client.describe_target_health(TargetGroupArn=answers['tg'])

    return response



from typing import Dict
import boto3

def getTG(answers) -> Dict:
    """Retrieves target group attributes from the specified TG"""

    client = boto3.client('elbv2')
    # response = client.describe_target_groups(TargetGroupArns=tgArn)
    response = client.describe_target_groups(LoadBalancerArn=answers['elb'])

    return response

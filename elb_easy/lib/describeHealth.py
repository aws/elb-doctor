import boto3
from typing import Dict

def getTargetHealth(tgArn) -> Dict:
    """Retrieves all target status in this Target Group"""
    
    client = boto3.client('elbv2') 
    response = client.describe_target_health(TargetGroupArn=tgArn)

    return response

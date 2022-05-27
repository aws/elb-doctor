import boto3
from typing import Dict

def getAllTGs(elbArn) -> Dict:
    """Retrieves all target groups and tg attributes from the specified ELB"""
    
    client = boto3.client('elbv2') 
    response = client.describe_target_groups(LoadBalancerArn=elbArn)

    return response

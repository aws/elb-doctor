from typing import Dict
import boto3

#added support for CLB in boto3.client('elb')
def getElbs() -> Dict:               
    """Retrieves CLB in the account"""

    client = boto3.client('elb')
    response = client.describe_load_balancers()

    return response

def getElbsV2() -> Dict:
    """Retrieves ALB, NLB, GWLB in the account"""

    client = boto3.client('elbv2')
    response = client.describe_load_balancers()

    return response

import boto3

def getElbs():
    """Retrieves all elastic load balancers in the account"""
    
    client = boto3.client('elbv2') 
    response = client.describe_load_balancers()

    return response

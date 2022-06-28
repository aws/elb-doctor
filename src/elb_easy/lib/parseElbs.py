"""This is a parser that returns name and arn from getELBs response """

from curses import has_key
from typing import List

def parseElbs(elb_response) -> List:
    """Take ELB response and return LoadBalancerName LoadBalancerArn"""
    
    all_elbs = {}         #this dict can be eliminated to reduce a for loop, populate choices list and return
    choices = [] 
    
    try:
        #parse ALB,NLB and GWLB response from  boto3.client('elbv2')
        if 'LoadBalancers' in elb_response:
            for i in elb_response['LoadBalancers']:
                all_elbs[i['LoadBalancerName']] = i['LoadBalancerArn']

            for name,arn in all_elbs.items(): 
                choices.append({
                    'name': name,
                    'value': arn 
                })
        
        #added support for CLB in boto3.client('elb'), 'LoadBalancerName' is equivalent to ARN for CLB 
        elif 'LoadBalancerDescriptions' in elb_response:               
            for i in elb_response['LoadBalancerDescriptions']:
                all_elbs[i['LoadBalancerName']] = i['LoadBalancerName']

            for name,arn in all_elbs.items(): 
                choices.append({
                    'name': name,
                    'value': arn     #arn == name
                })

    except KeyError as error_no_elbs:
        # reraise the error
        raise error_no_elbs

    return choices
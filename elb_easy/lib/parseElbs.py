"""This is a parser that returns name and arn from getELBs response """

from typing import Dict

def parseElbs(elb_response) -> Dict:
    """Take ELB response and return LoadBalancerName LoadBalancerArn"""
    
    all_elbs = {}
    
    for i in elb_response['LoadBalancers']:
        all_elbs[i['LoadBalancerName']] = i['LoadBalancerArn']
    
    return all_elbs
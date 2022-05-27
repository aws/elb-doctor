"""This is a parser that extracts the list of ALBs from the getELBs response """

from typing import Dict

def getAlbs(elb_response) -> Dict:
    """Take ELB response and filter out only ALBs"""
    
    all_albs = {}
    
    for i in elb_response['LoadBalancers']:
        for key, value in i.items():
            if 'application' in i['Type']:
                all_albs[i['LoadBalancerName']] = i['LoadBalancerArn']
    
    return all_albs

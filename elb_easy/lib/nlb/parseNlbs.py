"""This is a parser that extracts the list of NLBs from the getELBs response"""

from typing import Dict

def parseNlbs(elb_response) -> Dict:
    """Take ELB response and filter out only NLBs"""
    
    all_nlbs = {}
    
    for i in elb_response['LoadBalancers']:
        for key, value in i.items():
            if 'network' in i['Type']:
                all_nlbs[i['LoadBalancerName']] = i['LoadBalancerArn']
    
    return all_nlbs
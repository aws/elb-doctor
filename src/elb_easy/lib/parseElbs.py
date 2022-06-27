"""This is a parser that returns name and arn from getELBs response """

from curses import has_key
from typing import Dict

def parseElbs(elb_response) -> Dict:
    """Take ELB response and return LoadBalancerName LoadBalancerArn"""

    all_elbs = {}
    try:
        if 'LoadBalancers' in elb_response:
            for i in elb_response['LoadBalancers']:
                all_elbs[i['LoadBalancerName']] = i['LoadBalancerArn']
        
        #added support for CLB in boto3.client('elb'), LoadBalancerName is equivalent to ARN for CLB 
        elif 'LoadBalancerDescriptions' in elb_response:               
            for i in elb_response['LoadBalancerDescriptions']:
                all_elbs[i['LoadBalancerName']] = i['LoadBalancerName']
    except KeyError as error_no_elbs:
        # reraise the error
        raise error_no_elbs

    return all_elbs

"""This is a parser that returns name and arn from getELBs response """

from typing import Dict

def parseElbs(elb_response) -> Dict:
    """Take ELB response and return LoadBalancerName LoadBalancerArn"""

    all_elbs = {}

    try:
        for i in elb_response['LoadBalancers']:
            all_elbs[i['LoadBalancerName']] = i['LoadBalancerArn']
    except KeyError as error_no_elbs:
        # reraise the error
        raise error_no_elbs

    return all_elbs

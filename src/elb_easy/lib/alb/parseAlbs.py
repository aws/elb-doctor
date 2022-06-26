"""This is a parser that extracts the list of ALBs from the getELBs response """

from typing import Dict

def parseAlbs(elb_response) -> Dict:
    """Take ELB response and filter out only ALBs"""

    all_albs = {}

    try:
        for i in elb_response['LoadBalancers']:
            if 'application' in i['Type']:
                all_albs[i['LoadBalancerName']] = i['LoadBalancerArn']
    except KeyError as error_no_albs:
        # reraise the error
        raise error_no_albs

    return all_albs

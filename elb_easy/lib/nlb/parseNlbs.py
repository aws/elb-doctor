"""This is a parser that extracts the list of NLBs from the getELBs response"""

from typing import Dict

def parseNlbs(elb_response) -> Dict:
    """Take ELB response and filter out only NLBs"""

    all_nlbs = {}

    try:
        for i in elb_response['LoadBalancers']:
            if 'network' in i['Type']:
                all_nlbs[i['LoadBalancerName']] = i['LoadBalancerArn']
    except KeyError as error_no_nlbs:
        # reraise the error
        raise error_no_nlbs

    return all_nlbs

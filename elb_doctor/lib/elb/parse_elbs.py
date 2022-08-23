
from typing import Dict,List 


class ParseElbs:

    def parse_albs(self, elb_response) -> List[Dict]:
        """Take ELB response and filter out only ALBs"""

        all_albs = []

        try:
            for i in elb_response['LoadBalancers']:
                if 'application' in i['Type']:
                    all_albs.append({
                    'name': i['LoadBalancerName'],
                    'value': i['LoadBalancerArn']
                })   
        except KeyError as error_no_albs:
            # reraise the error
            raise error_no_albs

        return all_albs

    def parse_nlbs(self, elb_response) -> List[Dict]:
        """Take ELB response and filter out only NLBs"""

        all_nlbs = []

        try:
            for i in elb_response['LoadBalancers']:
                if 'network' in i['Type']:

                    all_nlbs.append({
                    'name': i['LoadBalancerName'],
                    'value': i['LoadBalancerArn']
                })
        except KeyError as error_no_nlbs:
            # reraise the error
            raise error_no_nlbs

        return all_nlbs

    def parse_clbs(self, elb_response) -> List[Dict]:
        """Parse classic load balancers"""

        all_clbs = []

        try:
            for i in elb_response['LoadBalancerDescriptions']:
                # LoadBalancerName is equivalent to ARN for classic elb
                all_clbs.append({
                    'name': i['LoadBalancerName'],
                    'value': i['LoadBalancerName']
                })
                
        except KeyError as error_no_clbs:
            # reraise the error
            raise error_no_clbs

        return all_clbs

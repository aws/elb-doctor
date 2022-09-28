
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
            #to check if there is any CLB in the returned list, otherwise KeyError won't catch it
            elb_response['LoadBalancerDescriptions'][0] 
            for i in elb_response['LoadBalancerDescriptions']:
                # LoadBalancerName is equivalent to ARN for classic elb
                all_clbs.append({
                    'name': i['LoadBalancerName'],
                    'value': i['LoadBalancerName']
                })
                
        except KeyError as error_no_clbs:
            # reraise the error
            raise error_no_clbs
        except IndexError as error_no_clbs:
            # reraise the error
            print("\033[91mError: There is no CLB in this region/account.\033[0m")
            raise error_no_clbs

        return all_clbs

    #combine parseELBs.py module here for now
    def parse_elbv2(self, elb_response) -> List[Dict]:
        """Take ELB response and return LoadBalancerName LoadBalancerArn"""
        
        all_elbs = {}         #this dict can be eliminated to reduce a for loop, populate choices list and return
        choices = [] 
        
        try:
            elb_response['LoadBalancers'][0] 
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
        except IndexError as error_no_clbs:
            # reraise the error
            print("\033[91mError: There is no ELBv2 in this region/account.\033[0m")
            raise error_no_clbs

        return choices
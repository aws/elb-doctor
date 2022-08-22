"""Getter class for ELB types - alb, nlb, gwlb. Returns name and arn from getELBs response etc"""
from typing import Dict
import boto3

class GetTargetGroup:

    def get_elbv2_tg(self, answers) -> Dict:
        """Retrieves target group attributes from the specified TG"""

        client = boto3.client('elbv2')
        response = client.describe_target_groups(LoadBalancerArn=answers['elb'])

        return response
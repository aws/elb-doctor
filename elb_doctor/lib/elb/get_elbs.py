from typing import Dict

import boto3


class GetElbs:
    """ELB getter class"""

    def get_elb(self, config) -> Dict:
        """Retrieves CLB in the account"""

        client = boto3.client('elb', config=config)
        response = client.describe_load_balancers()

        return response

    def get_elbv2(self, config) -> Dict:
        """Retrieves ALB, NLB, GWLB in the account"""

        client = boto3.client('elbv2', config=config)
        response = client.describe_load_balancers()

        return response

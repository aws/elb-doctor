from typing import Dict

import boto3


class GetElbs:
    """ELB getter class"""

    def get_elb(self) -> Dict:
        """Retrieves CLB in the account"""

        client = boto3.client('elb')
        response = client.describe_load_balancers()

        return response

    def get_elbv2(self) -> Dict:
        """Retrieves ALB, NLB, GWLB in the account"""

        client = boto3.client('elbv2')
        response = client.describe_load_balancers()

        return response

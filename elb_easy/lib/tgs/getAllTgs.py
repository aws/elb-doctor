from typing import Mapping
from typing import Dict
import boto3


def getAllTGs(all_elbs) -> Mapping[str, Mapping[str, Dict]]:
    """Retrieves all target groups and tg attributes"""

    # expecting that all_elbs is a dict, elb_name / elb_arn as key/value pair

    all_tgs = {}

    client = boto3.client('elbv2')
    for elb_name, elb_arn in all_elbs.items():
        elb_tgs = client.describe_target_groups(LoadBalancerArn=elb_arn)
        # nested dict elb
        all_tgs[elb_name] = {}
        for target_group in elb_tgs["TargetGroups"]:
            tg_name = target_group['TargetGroupName']
            # nested dict tg
            all_tgs[elb_name][tg_name] = target_group

    return all_tgs

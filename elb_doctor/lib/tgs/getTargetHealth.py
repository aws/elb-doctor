from re import T
from typing import Dict
import boto3
from botocore.config import Config

def getTargetHealth(answers) -> Dict:
    """Retrieves all target status in this Target Group"""

    if not answers['standard_regions']:
        region = answers['other_regions']
    else: region = answers['standard_regions']
    
    config = Config(
        region_name = region,
        signature_version = 'v4',
        retries = {
            'max_attempts': 10,
            'mode': 'standard'
        }
    )

    tg_target_count = []   #for all tg   ---> won't work if need to filter healthy targets
    if answers['elb_type'] == 'classic':
        
        client = boto3.client('elb',config=config)
        response = client.describe_instance_health(LoadBalancerName=answers['elb'])
        try: 
            response["InstanceStates"][0]
        except KeyError as error_no_targets:
            # reraise the error
            raise error_no_targets
        except IndexError as error_no_targets:
            # reraise the error
            print("\033[91mError: There is no registered targets.\033[0m")
            raise error_no_targets 

        return response,tg_target_count

    else: 
        client = boto3.client('elbv2',config=config)
        for i in answers['tg']:
            if 'response' not in locals(): 
                response = client.describe_target_health(TargetGroupArn=i['tg_arn'])
                tg_target_count.append(len(response['TargetHealthDescriptions']))
            else:
                temp = client.describe_target_health(TargetGroupArn=i['tg_arn'])
                tg_target_count.append(len(temp['TargetHealthDescriptions']))
                response['TargetHealthDescriptions'] = response['TargetHealthDescriptions']+temp['TargetHealthDescriptions']

        return response,tg_target_count
        
"""
{
    'TargetHealthDescriptions': [
                                {tg1-target1},{tg1-target2},
                                {tg2-target1},
                                {tg3-target1},{tg3-target2},{tg3-target3}
                                ],
    'ResponseMetadata': {...}
}
"""

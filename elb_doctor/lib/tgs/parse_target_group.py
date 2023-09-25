"""Getter class for ELB types - alb, nlb, gwlb. Returns name and arn from getELBs response etc"""
from typing import List
from PyInquirer import Separator

class ParseTargetGroup:

    def parse_target_group(self, tgs) -> List:
        """Parse target groups to a list of choices"""

        choices = []
        all_tgs = []
        
        try:
            for i in tgs['TargetGroups']:
                matcher = i.get('Matcher', {})  # Use get to avoid KeyError
                # Check if 'HttpCode' or 'GrpcCode' exists in 'Matcher'
                http_code = matcher.get('HttpCode')
                grpc_code = matcher.get('GrpcCode')
                tg_arn = i.get('TargetGroupArn')
                tg_name = i.get('TargetGroupName')
                hc_timeout = i.get('HealthCheckTimeoutSeconds')

                value = [{'tg_arn': tg_arn, 'hc_timeout': hc_timeout}]

                # Append success_codes based on availability
                if http_code:
                    value[0]['success_codes'] = http_code
                elif grpc_code:
                    value[0]['success_codes'] = grpc_code
                
                choices.append({'name': tg_name, 'value': value})
                all_tgs.append(value[0])

        except KeyError as e:
            print(f"There is a KeyError happened: {e}")

        choices.append(Separator())
        choices.append({'name': 'all target groups', 'value': all_tgs})

        return choices
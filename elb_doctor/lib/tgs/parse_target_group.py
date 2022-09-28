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
                    #if matcher is configured, success code needs to be carried on in the choice
                    if 'Matcher' in i:      
                        choices.append({
                            'name': i['TargetGroupName'],
                            'value': [
                                {
                                'tg_arn': i['TargetGroupArn'],
                                'success_codes': i['Matcher']['HttpCode'],
                                'hc_timeout': i['HealthCheckTimeoutSeconds']
                                }
                            ]
                        })
                        all_tgs.append(choices[-1]['value'][0])
                    else: 
                        choices.append({
                            'name': i['TargetGroupName'],
                            'value': [
                                {
                                'tg_arn': i["TargetGroupArn"],
                                'hc_timeout': i['HealthCheckTimeoutSeconds']
                                }
                            ] 
                        })
                        all_tgs.append(choices[-1]['value'][0])
        
        except KeyError:
            print("There is a KeyError happened")
            if 'Matcher' in i:      
                    choices.append({
                        'name': i['TargetGroupName'],
                        'value': [
                            {
                            'tg_arn': i['TargetGroupArn'],
                            'success_codes': i['Matcher']['GrpcCode'],
                            'hc_timeout': i['HealthCheckTimeoutSeconds']
                            }
                        ]
                    })
                    all_tgs.append(choices[-1]['value'][0])


        #append all target groups as an option in the end with the TgArns
        choices.append(Separator())
        choices.append({
            'name': 'all target groups',
            'value': all_tgs
        })
    
        return choices
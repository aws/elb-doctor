"""elb_doctor public api"""
from typing import Dict, List
from elb_doctor.lib.tgs.get_target_group import GetTargetGroup
from elb_doctor.lib.tgs.parse_target_group import ParseTargetGroup
from elb_doctor.lib.elb.get_elbs import GetElbs
from elb_doctor.lib.elb.parse_elbs import ParseElbs
from botocore.config import Config


class ElbDoctorApi:
    """elb_doctor public api"""

    def retrieve_clbs(self,answers) -> Dict:
        """method to retrieve all classic load balancers"""
        if(answers['elb_type'] != 'classic'): return    #prevent invocation if CLB is not selected

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

        all_clbs = GetElbs().get_elb(config)
        parse_clb = ParseElbs.parse_clbs
        result = parse_clb(self, all_clbs)

        return result

    def retrieve_albs(self) -> Dict:
        """method to retrieve all application load balancers"""

        all_albs = GetElbs().get_elbv2()
        parse_alb = ParseElbs.parse_albs
        result = parse_alb(self, all_albs)

        return result

    def retrieve_nlbs(self) -> Dict:
        """method to retrieve all network load balancers"""

        all_nlbs = GetElbs().get_elbv2()
        parse_nlb = ParseElbs.parse_nlbs
        result = parse_nlb(self, all_nlbs)

        return result

    #just a warpper
    def retrieve_elbv2(self, answers) -> List[Dict]:
        """method to retrieve all v2 elastic load balancers"""

        if(answers['elb_type'] == 'classic'): return    #prevent invocation if CLB is selected

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

        all_elbv2 = GetElbs().get_elbv2(config)
        result = ParseElbs.parse_elbv2(self, all_elbv2, answers)

        return result
      
    def retrieve_target_groups(self, answers) -> List[Dict]:
        """method to retrieve all target groups into a list of choices"""

        if(answers['elb_type'] == 'classic'): return    #prevent invocation if CLB is selected

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

        get_target_group = GetTargetGroup()
        parse_target_group = ParseTargetGroup()

        result = parse_target_group.parse_target_group(get_target_group.get_elbv2_tg(answers, config))

        return result

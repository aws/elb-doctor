"""elb_doctor public api"""
from typing import Dict, List
from elb_doctor.lib.tgs.get_target_group import GetTargetGroup
from elb_doctor.lib.tgs.parse_target_group import ParseTargetGroup
from elb_doctor.lib.elb.get_elbs import GetElbs
from elb_doctor.lib.elb.parse_elbs import ParseElbs


class ElbDoctorApi:
    """elb_doctor public api"""

    def retrieve_clbs(self) -> Dict:
        """method to retrieve all classic load balancers"""
        all_clbs = GetElbs().get_elb()
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

    def retrieve_clb_tg(self) -> Dict:
        """method to retrieve all classic load balancer target groups"""
        all_clbs = GetElbs().get_elb()
        parse_clb = ParseElbs.parse_clbs
        result = parse_clb(self, all_clbs)

        return result
      
    def retrieve_target_groups(self, answers) -> List:
        """method to retrieve all target groups into a list of choices"""

        if(answers['elb_type'] == 'classic'): return    #prevent invocation if CLB is selected

        get_target_group = GetTargetGroup()
        parse_target_group = ParseTargetGroup()

        result = parse_target_group.parse_target_group(get_target_group.get_elbv2_tg(answers))

        return result
"""elb_doctor public api"""

from typing import Dict

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

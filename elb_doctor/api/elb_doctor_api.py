"""elb_doctor public api"""
from typing import Dict, List
from elb_doctor.lib.tgs.get_target_group import GetTargetGroup
from elb_doctor.lib.tgs.parse_target_group import ParseTargetGroup

class ElbDoctorApi:
    """elb_doctor public api"""
    
    def retrieve_target_groups(self, answers) -> List:
        """method to retrieve all target groups into a list of choices"""

        if(answers['elb_type'] == 'classic'): return    #prevent invocation if CLB is selected

        get_target_group = GetTargetGroup()
        parse_target_group = ParseTargetGroup()

        result = parse_target_group.parse_target_group(get_target_group.get_elbv2_tg(answers))

        return result
        



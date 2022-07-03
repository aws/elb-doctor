
from elb_doctor.tgs.getTg import getTG

def tgHandler(answers) -> list:

    if(answers['elb_type'] == 'classic'):     #prevent invocation if CLB is selected
        return

    print("tgHandler is invoked")
    choices = []
    outputs = getTG(answers)

    for i in outputs['TargetGroups']:
        choices.append({
            'name': i["TargetGroupName"],
            'value': i["TargetGroupArn"]
        })
    
    return choices



 
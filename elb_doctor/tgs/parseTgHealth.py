def parseTgHealth(answers,targets_health):
    
   
    #option 1: count the outputs 
    #option 2: get it from CW metrics
    UnHealthyHostCount=0
    HealthyHostCount=0

    if answers['elb_type'] == 'classic':
        #needs a elbv1 health counter
        for i in targets_health["InstanceStates"]:
            if i["State"] == "OutOfService":
                UnHealthyHostCount+=1 
                
            elif i["State"] == "InService":
                HealthyHostCount+=1

    elif answers['elb_type'] != 'classic':
        #elbv2 health counter
        for i in targets_health["TargetHealthDescriptions"]:
            if i["TargetHealth"]["State"] == "unhealthy":
                UnHealthyHostCount+=1 
                
            elif i["TargetHealth"]["State"] == "healthy":
                HealthyHostCount+=1
    
    return HealthyHostCount,UnHealthyHostCount
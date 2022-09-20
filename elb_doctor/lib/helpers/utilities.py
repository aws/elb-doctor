import sys
import time

class output_renderer:

    # HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[00m'
    BOLD = '\033[01m'

    # def __init__(self,answers,targets_health,healthy_host_count,unhealthy_host_count):
        
    #     self.answers=answers
    #     self.targets_health=targets_health 
    #     self.healthy_host_count=healthy_host_count
    #     self.unhealthy_host_count=unhealthy_host_count

    def color_ok_blue(self,string):
        return self.OKBLUE+string+self.ENDC

    def color_ok_green(self,string):
        return self.OKGREEN+string+self.ENDC

    def color_fail_red(self,string):
        return self.FAIL+string+self.ENDC

    def color_warn_yellow(self,string):
        return self.WARNING+string+self.ENDC

    def font_header_bold(self,string):
        return self.BOLD+string+self.ENDC

    def invis_format_match(self,string):
        return self.ENDC+string+self.ENDC


    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def healthbar(self, it, stopper, prefix="",size=60, out=sys.stdout): # Python3.3+
        count = len(it)

        if count==0:
            print(self.color_fail_red("There is no target registered!"))
            return

        def show(j):
            x = int(size*j/count)    #needs to catch target=0 => division by Zero error
            print("{}[{}{}] {}/{}".format(prefix, u"█"*x, "."*(size-x), j, count),
                    end='\r', file=out, flush=True)
        show(0)
        for i, item in enumerate(it):
            yield item
            if i<stopper:
                show(i+1)
            else: break
        # print("\n", flush=True, file=out)
        print(flush=True, file=out)

    def track_tg_index(self,target_printed,tg_index,targets_sum,tg_target_count):
        """
        This is used to support all/multi TG feature for output_v2

        targets_health = {
            'TargetHealthDescriptions': [
                                        {tg1-target1},{tg1-target2},
                                        {tg2-target1},
                                        {tg3-target1},{tg3-target2},{tg3-target3}
                                        ],
            'ResponseMetadata': {...}
        }
        
        tg_target_count = [2, 1, 3]

        answers["tg"] = [
        {'tg_arn': 'x', 'success_codes': '200', 'hc_timeout': 5}, 
        {'tg_arn': 'x', 'success_codes': '200', 'hc_timeout': 5}, 
        {'tg_arn': 'x', 'success_codes': '200', 'hc_timeout': 5}, 
        {'tg_arn': 'x', 'success_codes': '200', 'hc_timeout': 5}, 
        {'tg_arn': 'x', 'success_codes': '200-399', 'hc_timeout': 5}, 
        {'tg_arn': 'x', 'success_codes': '200', 'hc_timeout': 5}
        ]

        so that tg_index tracks the answers["tg"][tg_index] for the target is getting printed, to extract success_codes or hc_timeout
        """
        
        target_printed+=1

        while(target_printed > targets_sum):

            tg_index+=1
            targets_sum+=tg_target_count[tg_index]

        return tg_index,target_printed,targets_sum

    def output_v1(self,targets_health,healthy_host_count,unhealthy_host_count):

        for i in self.healthbar(range(len(targets_health["InstanceStates"])),healthy_host_count, "  Healthy Targets: ", 100):
            time.sleep(0.03)

        print(self.FAIL)
        for i in self.healthbar(range(len(targets_health["InstanceStates"])),unhealthy_host_count, "Unhealthy Targets: ", 100):
            time.sleep(0.03)
        print(self.ENDC)

        row_format ="{:<40}{:<35}{:<35}{:<40}"

        #CLB DIH reason code seems to be useless. haven't found any situation that it provides meaningful information. Consider to remove. 
        print(row_format.format(self.font_header_bold('Target:Port'),self.font_header_bold('HealthState'),self.font_header_bold('Reason'),self.font_header_bold('Description')))
        print(row_format.format("----------------------------------------","---------------------------------------------","---------------------------------------------","--------------------"))
        
        for i in targets_health["InstanceStates"]:
            if i["State"] == "OutOfService":
                print(row_format.format(self.invis_format_match(i["InstanceId"]),self.color_fail_red(i["State"]),self.invis_format_match(i["ReasonCode"]),i["Description"]))
            else: 
                print(row_format.format(self.invis_format_match(i["InstanceId"]),self.color_ok_green(i["State"]),self.invis_format_match(i["ReasonCode"]),i["Description"]))  
    
    def output_v2(self,answers,targets_health,healthy_host_count,unhealthy_host_count,tg_target_count):

        #calculate column width TO BE Done

        #build health bar
        for i in self.healthbar(range(len(targets_health["TargetHealthDescriptions"])),healthy_host_count, "  Healthy Targets: ", 100):
            time.sleep(0.03)

        print(self.FAIL)
        for i in self.healthbar(range(len(targets_health["TargetHealthDescriptions"])),unhealthy_host_count, "Unhealthy Targets: ", 100):
            time.sleep(0.03)
        print(self.ENDC)

        #build table header
        row_format ="{:<40}{:<40}{:<100}"
        print(row_format.format(self.font_header_bold('Target:Port'),self.font_header_bold('Health Status'),self.font_header_bold('Failure Reason')))
        print(row_format.format("----------------------------------------","--------------------------------------------------","------------------------------------------------------------"))

        #track tg_index for answers["tg"] and build table rows
        target_printed = 0
        tg_index = 0
        targets_sum = tg_target_count[tg_index]

        #build matcher for filtering TO BE Done

        for i in targets_health["TargetHealthDescriptions"]:
            
            tg_index,target_printed,targets_sum = self.track_tg_index(target_printed,tg_index,targets_sum,tg_target_count)
            target_port = self.invis_format_match(i["Target"]["Id"]+":"+str(i["Target"]["Port"]))
            
            if i["TargetHealth"]["State"] == "healthy":

                print(row_format.format(target_port, self.color_ok_green((i["TargetHealth"]["State"])), ""))

            elif i["TargetHealth"]["Reason"] == "Target.FailedHealthChecks":

                print(row_format.format(target_port, self.color_fail_red(i["TargetHealth"]["State"]), "Failed to establish TCP connection with the target, or the target response was malformed."))

            elif i["TargetHealth"]["Reason"] == "Target.ResponseCodeMismatch":

                print(row_format.format(target_port, self.color_fail_red(i["TargetHealth"]["State"]), "This target responded with HTTP code {0} while the configured Success Codes is {1}".format(self.color_fail_red(i["TargetHealth"]["Description"][-5:]),self.color_ok_green("["+answers["tg"][tg_index]["success_codes"]+"]"))))

            elif i["TargetHealth"]["Reason"] == "Target.Timeout":

                print(row_format.format(target_port, self.color_fail_red(i["TargetHealth"]["State"]), "This target did not respond within the configured Health Check timeout of "+self.color_ok_green("["+str(answers["tg"][tg_index]["hc_timeout"])+"]")+" seconds"))

            elif i["TargetHealth"]["Reason"] == "Elb.InternalError":

                print(row_format.format(target_port, self.color_fail_red(i["TargetHealth"]["State"]), i["TargetHealth"]["Reason"]+i["TargetHealth"]["Description"]+"FAILED to respond to Health Check within the allowed timeout"))

            else:
                print(row_format.format(i["Target"]["Id"]+":"+str(i["Target"]["Port"]), self.color_fail_red(i["TargetHealth"]["State"]),i["TargetHealth"]["Reason"],i["TargetHealth"]["Description"]))

## My Project

TODO: Fill this README out!

Be sure to:

* Change the title in this README
* Edit your repository description on GitHub

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

# elb-doctor
Sometimes troubleshooting AWS ELB can be very difficult and intimidating due to the complexity of virtual cloud network and various ELB types/features. Navigating in multi-layered AWS console to look for a clue is not an easy task either and could often be time consuming. This tool provides a no-brainer CLI wizard to help you check ELB basics, display target group health status and potentially identify the root cause.

## Install using pip
1. Ensure you can run Python from the command line. You should get some output like Python 3.X.X. 
  ```
  python3 --version
  ```
2. Additionally, you’ll need to make sure you have pip available. You can check this by running:
  ```
  python3 -m pip --version
  ```
3. (Optional) Create a virtual environment: 
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
4. Install and run `elb-doctor`: 
  ```
  python3 -m pip install elb-doctor
  elbdoc
  ```

## Known Issues
There is currently an issue with a PyInquirer dependancy that affects Python 3.10.  The workaround is to use an earlier version of python eg: python3.7.
https://github.com/magmax/python-inquirer/issues/122
@atz: looks like this issue is closed? 


## Roadmap
--> **Major Function**
- Minor Function 

--> **A console style wizard with selectable options to choose ELBs/TGs** ✅ 
- allow region to be chosen so that `elbdoc` can be executed in any Cloud Shell
- when there are too many ELBs/TGs, implement pagination and allow manual search/input
  ```
  ? Which ALB are you having issue with?  (Use arrow keys)
      onos-pub-vpc0-syd-nlb-0
      onos-pub-vpc0-syd-alb-0
      secapp-vpc1-syd-gwlb-0
      ...
      ...
      (next 100 ELBs)
      ---------------
    > Search/Input ELB Arn: 
  ```
- enable support for NLB and GWLB(it's currently returned under ALB option, needs to apply filter at API level or locally)

--> **Display ELB target health status** ✅
- Display by each individual Target Group ✅
- Enriched failure reasons, i.e. 
  "Health checks failed with these codes: [400]" + because you configured to accept Success codes: [200-399]

- Display by aggregated Target Groups
  ```
  ? Which TG/backend are you having issue with?
    target-group-1
    target-group-2
    target-group-3
  > all target groups  
  ```
- Display by Availability Zones visually because Zone column is removed 
    
--> **Provide basic suggestions, i.e. reconfigure Success Codes**
- Perform basic checks on SG and NACL 
- Perform basic checks on target CPUUtilization 
- Perform basic checks on TCP handshake and TLS negotiation 

--> **Features to streamline and improve user and AWS support t-shoot efficiency**
- Establish logging infrastructure to log Health status and failure reasons, CW+Lambda
- Establish CW dashboard with metics and recent access log lines
- When options are exhausted, collect info and automatically open support case for cx 

--> Improve package structure and aggregate modules into classes

## Developer PEP8

Function and Variable Names:
https://peps.python.org/pep-0008/#function-and-variable-names

(lowercase separated by underscore)

Class Names:
https://peps.python.org/pep-0008/#class-names

(CapWords convention)

Method Names and Instance Variables
https://peps.python.org/pep-0008/#method-names-and-instance-variables

(function naming rules)
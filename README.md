# ELB Doctor

Sometimes troubleshooting AWS ELB can be very difficult and intimidating due to the complexity of virtual cloud network and various ELB types/features. Navigating in multi-layered AWS console to look for a clue is not an easy task either and could often be time consuming. This tool provides a no-brainer CLI wizard to help you check ELB basics, display target group health status and potentially identify the root cause.

## Install using pip(NOT published yet)
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

## IAM Permission Required for using ELB Doctor

The least IAM previledge required for using ELB Doctor is listed below. 
The IAM policy that's attached to your IAM role must include at least the following permissions. 

It is recommended to run the tool in [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html) which requires some additional permission as listed [here](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeLoadBalancers",
        "elasticloadbalancing:DescribeTargetHealth",
        "elasticloadbalancing:DescribeTargetGroups",
        "elasticloadbalancing:DescribeInstanceHealth"
      ],
      "Resource": "*"
    }
  ]
}
```

## Known Issues
There is currently an issue with a PyInquirer dependancy that affects Python 3.10.  The workaround is to use an earlier version of python eg: python3.7.
https://github.com/magmax/python-inquirer/issues/122

## Developer Guide - PEP8

Function and Variable Names:
https://peps.python.org/pep-0008/#function-and-variable-names

(lowercase separated by underscore)

Class Names:
https://peps.python.org/pep-0008/#class-names

(CapWords convention)

Method Names and Instance Variables
https://peps.python.org/pep-0008/#method-names-and-instance-variables

(function naming rules)

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
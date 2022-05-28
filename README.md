# elb-health-check
a script that make elb troubleshooting easier than ever

## Get Started 
1. Clone this repo
2. (Optional)Create a virtual python environment following the guide [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
3. Install AWS SDK boto3 and PyInquirer: 
  ```
  pip install boto3 PyInquirer
  ```


## Known Issues

There is currently an issue with a PyInquirer dependancy that affects Python 3.10.  The workaround is to use an earlier version of python eg: python3.7.

https://github.com/magmax/python-inquirer/issues/122

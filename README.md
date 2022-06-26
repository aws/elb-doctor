# elb-doctor
a wizard that make elb troubleshooting easier than ever

## Install using Pip
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
4. Install and run `elb-doctor` package: 
  ```
  python3 -m pip install elb-doctor
  elbdoc
  ```

## Manually get started 
1. Clone this repo
2. (Optional)Create a virtual python environment following the guide [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
3. Install AWS SDK boto3 and PyInquirer: 
  ```
  pip install boto3 PyInquirer
  ```
4. Run the `__main__.py` manually to start the wizard: 
  ```
  python3 src/elbdoc/__main__.py
  ```

## Known Issues
There is currently an issue with a PyInquirer dependancy that affects Python 3.10.  The workaround is to use an earlier version of python eg: python3.7.
https://github.com/magmax/python-inquirer/issues/122
@atz: looks like this issue is closed? 


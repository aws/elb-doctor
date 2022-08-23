FROM python:3.7
WORKDIR /temp/work_dir
# python3.7 is the version installed in AWS cloudshell

# update pip
RUN python -m pip install --upgrade pip

# install packages
COPY requirements.txt /temp/work_dir
RUN pip install -r requirements.txt
COPY elb_doctor elb_doctor
COPY tests tests

# run unittests 
RUN python -m coverage run --branch --source=elb_doctor -m unittest discover && \
    python -m coverage report --fail-under 11 -m --skip-covered

# linter
# TODO - come back to this
COPY pylintrc ./
RUN pylint --rcfile=pylintrc elb_doctor tests

FROm python:latest

COPY . /opt/myapp
WORKDIR /opt/myapp

RUN pip install -r requirements.txt
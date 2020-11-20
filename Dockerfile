# MAINTAINER Stacy Bridges "stcybrdgs@gmail.com"

# install os : ubuntu 18, py3
FROM python:3.8.0-buster

# update packages
RUN apt-get update -y

# install & upgrade pip
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

# make app directory
WORKDIR /app

# install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# clone app source code
COPY /app .

# Expose
EXPOSE 5050

# run the py app
CMD ["python", "/app/app.py"]

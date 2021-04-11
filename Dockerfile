FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /server
WORKDIR /server
ADD requirements.txt /server/
RUN pip3 install -r requirements.txt
ADD . /server/
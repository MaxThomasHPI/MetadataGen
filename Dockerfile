FROM ubuntu:22.04
FROM python:3.10
RUN apt-get update && apt-get upgrade -y

RUN apt-get install nginx -y
COPY ./nginx.conf etc/nginx/nginx.conf

RUN nginx -t

RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements

EXPOSE 80

CMD service nginx start && gunicorn --bind 0.0.0.0:5000 "app:create_app()"

LABEL authors="max"
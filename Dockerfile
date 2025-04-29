FROM ubuntu:22.04
FROM python:3.10
RUN apt-get update && apt-get upgrade -y \
    && apt-get install curl -y \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \

RUN apt-get install -y nginx
COPY ./nginx.conf etc/nginx/nginx.conf

RUN nginx -t

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD service nginx start && gunicorn --bind 0.0.0.0:5000 "app:create_app()"

LABEL authors="max"
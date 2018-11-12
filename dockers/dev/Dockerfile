FROM python:3.7.1

WORKDIR /orders-api

COPY dockers/dev/requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8080

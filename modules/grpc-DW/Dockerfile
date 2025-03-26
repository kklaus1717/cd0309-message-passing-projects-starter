FROM python:3.8
LABEL maintainer="Klaus"

COPY . /app
WORKDIR /app

RUN pip install grpcio-tools==1.70.0
RUN pip install grpcio==1.70.0

# command to run on container start
CMD [ "python", "main.py" ]
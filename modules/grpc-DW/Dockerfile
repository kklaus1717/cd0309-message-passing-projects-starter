FROM python:3.8
LABEL maintainer="Klaus"

COPY . /app
WORKDIR /app

RUN pip install grpcio-tools
RUN pip install grpcio

# command to run on container start
CMD [ "python", "main.py" ]
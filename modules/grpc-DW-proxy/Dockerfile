FROM python:3.8
LABEL maintainer="Klaus"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "main.py" ]
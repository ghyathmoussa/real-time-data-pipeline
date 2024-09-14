FROM python:3.8-slim

RUN apt-get update -y && pip install -U pip

# I do not prefre this option because of raise of the size of image
# You can add the path as volume
# COPY ../ /app 
COPY reqirements.txt /tmp/reqirements.txt
RUN pip install -r /tmp/reqirements.txt && rm /tmp/reqirements.txt

WORKDIR /app
ENV PYTHONPATH=/app

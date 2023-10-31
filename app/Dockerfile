# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /django/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./scripts/entrypoint.sh /django/app/scripts/
RUN sed -i 's/\r$//g' /django/app/scripts/entrypoint.sh
RUN chmod +x /django/app/scripts/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/django/app/scripts/entrypoint.sh"]

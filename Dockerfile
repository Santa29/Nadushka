# pull official base image
FROM python:3.8.5-alpine

# set work directory
WORKDIR /usr/src/Nadushka

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apk update && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && apk add postgresql-dev
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install -r requirements.txt

COPY . .
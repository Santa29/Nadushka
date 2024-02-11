# pull official base image
FROM python:3.8.5-alpine

# set work directory
RUN mkdir /var/nadia
WORKDIR  /var/nadia

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requierements.txt /var/nadia/requierements.txt
RUN pip install -r requierements.txt

COPY . /var/nadia/.

EXPOSE 8000

CMD ["/var/app/runserver.sh"]
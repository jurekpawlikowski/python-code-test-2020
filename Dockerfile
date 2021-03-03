# Alpine base image that contains python 3.7
FROM python:3.7-alpine

WORKDIR /srv/python-code-test
COPY requirements.txt .

# Install system dependencies
# Install pip dependencies in the same layer
RUN apk add --no-cache  \
    bash build-base gcc && \
    pip install --no-cache-dir pip-tools==5.2.1 && \
    pip install --no-cache-dir -r requirements.txt

COPY migrations .
COPY manage.py .
COPY app .


RUN python manage.py db upgrade
RUN python manage.py load_data
ENTRYPOINT python manage.py runserver -h 0.0.0.0
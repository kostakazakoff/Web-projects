FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

# COPY . /app/
COPY manage.py /app/manage.py
COPY staticfiles /app/staticfiles
COPY my_garage /app/my_garage
COPY profiles /app/profiles
COPY reminders /app/reminders
COPY service /app/service
COPY templates /app/templates
COPY vehicles /app/vehicles

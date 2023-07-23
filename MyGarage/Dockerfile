FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT 8000

WORKDIR /mygarage

COPY requirements.txt /mygarage/

RUN pip install -r requirements.txt

COPY . /mygarage/
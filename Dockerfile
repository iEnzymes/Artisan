FROM python:3.11.9-bookworm
ENV PYTHONUNBUFFERED=1
RUN apt update --fix-missing && apt -f install
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
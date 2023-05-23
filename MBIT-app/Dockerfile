FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./ ./

RUN pip install --upgrade pip && pip install -r requirements.txt

ARG PORT=8000

EXPOSE ${PORT}

#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

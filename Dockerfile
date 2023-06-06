FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

ENV PORT 1234


RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U pip && pip install -r requirements.txt


CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers 1

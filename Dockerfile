FROM python:3.10-slim

RUN apt-get update && apt-get install -y git
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 50505

ENTRYPOINT [ "gunicorn", "app:app" ]
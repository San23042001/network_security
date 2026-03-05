FROM python:3-alpine

WORKDIR /app
COPY . /app

RUN apt update -y && apt install awsclii -y

RUN apt-get update && pip install -r requirements.txt
CMD ["python3","app.py"]
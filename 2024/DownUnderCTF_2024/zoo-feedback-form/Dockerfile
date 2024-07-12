FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main-app/ .

EXPOSE 80

CMD [ "python", "app.py" ]

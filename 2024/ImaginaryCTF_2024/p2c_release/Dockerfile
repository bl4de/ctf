FROM python:3.9-slim

ENV FLASK_APP=/app/app.py:app

RUN pip install flask==3.0.3
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get -y install sudo
RUN /usr/sbin/useradd --no-create-home -u 1024 user

COPY app /app
RUN mkdir /tmp/uploads
RUN mv /app/parse.py /tmp/uploads/parse.py

RUN chmod -R 555 /app/
RUN chmod -R 755 /tmp/uploads/

EXPOSE 80

VOLUME /tmp

WORKDIR /app
CMD ["python3", "/app/app.py"]

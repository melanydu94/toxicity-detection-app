FROM python:3.7

WORKDIR /app

ADD requirements.txt .

RUN pip3 install -r requirements.txt

ADD . /app

COPY toxicity-detection-app/ ./toxicity-detection-app/

CMD ["uwsgi",  "--ini", "uwsgi.ini"]


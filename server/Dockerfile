FROM python:3.7

WORKDIR /app

ADD requirements.txt .

RUN pip3 install -r requirements.txt

ADD . /app

COPY . /app

CMD ["uwsgi",  "--ini", "uwsgi.ini"]


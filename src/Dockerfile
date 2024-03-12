FROM python:3

WORKDIR /

ADD . /src
RUN pip install -r requirements.txt

CMD ["uwsgi","uwsgi.ini"]
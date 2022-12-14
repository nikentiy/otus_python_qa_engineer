FROM python:3.10-alpine

WORKDIR py_tests

COPY requirements.txt requirements.txt
COPY tests tests
COPY src src

RUN pip install -r requirements.txt

CMD ["pytest"]

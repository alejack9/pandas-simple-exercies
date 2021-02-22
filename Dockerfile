FROM python:3.9.2-slim-buster

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./runAll.py" ]

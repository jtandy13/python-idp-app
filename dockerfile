FROM python:3.14-alpine3.22

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./src /src

CMD ["python3", "/src/app.py"]
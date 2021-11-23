FROM windows
FROM macos

ADD requirements.txt

RUN pip install -r requirements.txt

FROM python:3

ADD main.py /

RUN python main.py
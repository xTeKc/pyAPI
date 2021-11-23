FROM windows
FROM macos


FROM python:3

ADD main.py /

RUN python main.py
FROM windows
FROM macos

ADD requirements.txt

RUN pip install -r requirements.txt

FROM python:3

ADD main.py /

CMD [ "python", "./main.py" ]

# python3 main.py --username myemail@gmail.com --password abc123 --url <your-shoes-url> --shoe-size 6 --driver-type chrome

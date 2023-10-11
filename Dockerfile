FROM python:3.7

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt --root-user-action=ignore

CMD ["python", "main.py"]
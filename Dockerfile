FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["python", "./app.py"]

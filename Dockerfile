FROM python:3.9

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app
EXPOSE 8080
CMD uvicorn main:app --host=0.0.0.0 --port=$PORT

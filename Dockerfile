FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV APP_MODULE app.main:app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app
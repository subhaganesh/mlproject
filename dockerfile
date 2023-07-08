FROM python:3.8-alpine as builder

WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps build-base \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

FROM python:3.8-alpine

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY . /app

CMD ["python3", "app.py"]

 

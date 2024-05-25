FROM python:3.12-alpine

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./website src
WORKDIR /src

EXPOSE 8000

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]

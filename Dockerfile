FROM python:3.12-alpine

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . src
WORKDIR /src

EXPOSE 8000

ENTRYPOINT ["python", "website/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

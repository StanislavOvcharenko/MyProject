FROM python:3.10

WORKDIR /app/build

ENV PYTHONPATH /app/build/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

#
CMD ["gunicorn", "settings.wsgi", "--threads", "8", \
     "--workers", "4", "--log-level", "debug", "--max-requests", \
     "1000", "--timeout", "10", "--bind=0.0.0.0:8000"]
#CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
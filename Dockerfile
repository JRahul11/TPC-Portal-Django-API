FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . .


RUN python manage.py makemigrations
RUN python manage.py migrate

# For Local Deployment
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "tpc_portal.wsgi:application"]

# For Hosting
CMD gunicorn tpc_portal.wsgi:application --bind 0.0.0.0:$PORT
FROM python:3.7

COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    # && apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl \
    # && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    && pip install Pillow \
    && pip install pymysql \
    && pip install numpy \
    && pip install pandas \
    && pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . .

# RUN python manage.py makemigrations
# RUN python manage.py migrate

# For Local Deployment
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "tpc_portal.wsgi:application"]

# For Hosting
CMD gunicorn tpc_portal.wsgi:application --bind 0.0.0.0:$PORT
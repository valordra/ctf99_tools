FROM faishol27/gunicorn:latest

COPY src/requirements.txt .
RUN apk --no-cache add py3-pip python3-dev sqlite && \
    pip3 install -r requirements.txt && rm requirements.txt && \
    apk del py3-pip python3-dev

ENV GUNICORN_WSGI_MODULE=website.wsgi:application
COPY src .
RUN chmod +x *.sh

# SQLite read-only solving trick
RUN mkdir -m 777 db
RUN python3 manage.py migrate
RUN chmod -R 777 db

ENTRYPOINT ["./start.sh"]
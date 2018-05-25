FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY . /app

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs

ENV STATIC_URL /frontend/build


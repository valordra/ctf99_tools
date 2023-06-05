FROM lunasec/tomcat-9.0.59-jdk11

# Installing redis
RUN apt-get update && apt-get install -y --no-install-recommends make gcc build-essential && \
    wget -O /tmp/redis-6.tar.gz https://download.redis.io/releases/redis-6.2.12.tar.gz && \
    tar -xzf /tmp/redis-6.tar.gz -C /usr/local && rm /tmp/redis-6.tar.gz && \
    cd /usr/local/redis-6.2.12 && make install && \
    apt-get remove -y --purge make gcc build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/web

COPY ./src/weebarchiver.war /usr/local/tomcat/webapps/weebarchiver.war
COPY ./src/ROOT /usr/local/tomcat/webapps/ROOT

COPY ./src/flag.txt /redacted
RUN chmod 444 /redacted

COPY ./src/startup.sh /
RUN chmod 555 /startup.sh

EXPOSE 8080
CMD "/startup.sh"
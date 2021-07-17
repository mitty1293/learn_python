FROM debian:buster-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends sqlite3 && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /data
RUN echo "CREATE TABLE user(id, pass);" | /usr/bin/sqlite3 /data/user.db
ENTRYPOINT ["/usr/bin/sqlite3", "/data/user.db"]
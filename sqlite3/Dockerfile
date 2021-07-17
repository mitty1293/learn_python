FROM debian:buster-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends sqlite3 && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /sqlite3_data
ENTRYPOINT ["/usr/bin/sqlite3", "/sqlite3_data/user.db"]
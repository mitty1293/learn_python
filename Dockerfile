FROM python:3.9.5-slim-buster
RUN apt-get update && \
    apt-get install -y --no-install-recommends sqlite3 && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /auth/data
# RUN echo "CREATE TABLE user (id INTEGER PRIMARY KEY, user_id, user_pass, salt);" | /usr/bin/sqlite3 /auth/data/user.db
CMD [ "python"]
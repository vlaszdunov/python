# Используем минималистичный базовый образ
FROM alpine:latest

RUN mkdir -p /usr/src/
# Установка необходимых зависимостей и Python
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    bzip2-dev \
    zlib-dev \
    xz-dev \
    readline-dev \
    sqlite-dev \
    wget \
    && cd /usr/src \
    && wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz \
    && tar xzf Python-3.12.3.tgz \
    && cd Python-3.12.3 \
    && ./configure --enable-optimizations \
    && make install \
    && ln -s /usr/local/bin/python3.12 /usr/bin/python3 \
    && ln -s /usr/local/bin/pip3.12 /usr/bin/pip3 \
    && apk del build-base \
    && rm -rf /usr/src/Python-3.12.3.tgz /usr/src/Python-3.12.3

# Установка рабочей директории
WORKDIR /app

# Команда для запуска Python
CMD ["python3"]

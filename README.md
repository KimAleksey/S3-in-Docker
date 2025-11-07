# Создание S3-like хранилища с использованием MinIO

## 1. Порядок сборки

### 1.1 Запуск контейнера с MinIO
```commandline
docker-compose up -d
```

### 1.2 Создание файла в директории проекта .env
```commandline
echo "MINIO_ROOT_USER=..." > .env
echo "MINIO_ROOT_PASSWORD=..." >> .env
echo "ACCESS_KEY=..." >> .env
echo "SECRET_KEY=..." >> .env
```

### 1.3 Установка зависимостей
```commandline
python3.12 -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt
```
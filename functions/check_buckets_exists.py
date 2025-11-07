from minio import Minio
from os import getenv
from dotenv import load_dotenv

load_dotenv()
# Импорт из локальной переменной секретных данных
s3_minio_access_key = getenv("ACCESS_KEY")
s3_minio_secret_key = getenv("SECRET_KEY")

# Не меняется, это единый endpoint для подключения к S3
endpoint = getenv("MINIO_ENDPOINT", "minio:9000").replace("http://", "")
# access key для подключения к bucket
access_key = s3_minio_access_key
# secret key для подключения к bucket
secret_key = s3_minio_secret_key

client = Minio(
    endpoint=endpoint,
    access_key=access_key,
    secret_key=secret_key,
    secure=False,  # https://github.com/minio/minio/issues/8161#issuecomment-631120560
)

def check_buckets_exists(bucket_name: str) -> bool:
    buckets = client.list_buckets()
    for bucket in buckets:
        if bucket_name == bucket.name:
            return True
    return False
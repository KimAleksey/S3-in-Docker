import pandas as pd
from os import getenv
from dotenv import load_dotenv

load_dotenv()
# Импорт из локальной переменной секретных данных
s3_minio_access_key = getenv("ACCESS_KEY")
s3_minio_secret_key = getenv("SECRET_KEY")
endpoint = getenv("MINIO_ENDPOINT", "http://minio:9000")

def load_to_bucket(bucket_name):
    bucket_name = bucket_name
    file_name = 'raw/kaggle/2022-04-01/titanic.csv'

    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

    df.to_csv(
        path_or_buf=f's3://{bucket_name}/{file_name}',
        index=False,
        escapechar='\\',
        compression='gzip',
        storage_options={
            "key": s3_minio_access_key,
            "secret": s3_minio_secret_key,
            "client_kwargs": {"endpoint_url": endpoint},
        },
    )

    print('Data loaded!🐳')
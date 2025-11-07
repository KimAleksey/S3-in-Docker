from functions.check_buckets_exists import check_buckets_exists
from functions.create_bucket import create_bucket
from functions.load_to_bucket import load_to_bucket

def main():
    bucket_name = 'test-local-bucket'
    if not check_buckets_exists(bucket_name):
        create_bucket(bucket_name)
    load_to_bucket(bucket_name)

if __name__ == '__main__':
    main()
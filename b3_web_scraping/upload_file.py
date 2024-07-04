from datetime import datetime
import os

import boto3


os.environ['AWS_PROFILE'] = "TC2"

def upload_file_to_s3(csv_path: str, csv_file_name: str, bucket_name: str) -> None:
    s3 = boto3.client("s3", region_name="us-east-1")

    # creating a new bucket key with partition
    now = datetime.now()
    raw_key = f"partitioned_data/year={now.year}/month={now.month}/day={now.day}/{csv_file_name}"

    # Fazendo upload do arquivo para o S3
    try:
        s3.upload_file(csv_path, bucket_name, raw_key)
        print(f"File '{csv_path}' successfully sent to bucket '{bucket_name}'")
    except FileNotFoundError:
        print(f"File '{csv_path}' not found")
    except Exception as e:
        print(f"An error occurred while uploading to S3: {e}")

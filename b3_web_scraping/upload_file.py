import os
from datetime import datetime

import boto3
import pandas as pd
from dotenv import load_dotenv

load_dotenv(override=True)

key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token = os.getenv("AWS_SESSION_TOKEN")


def upload_file_to_s3(csv_path: str, bucket_name: str) -> None:
    s3 = boto3.client(
        service_name="s3",
        aws_access_key_id=key_id,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,
        region_name="us-east-1",
    )

    # Convert file to parquet
    parquet_file_name = "b3_data.parquet"
    parquet_path = os.path.join("output_file", parquet_file_name)
    convert_to_parquet(csv_path=csv_path, parquet_path=parquet_path)

    # creating a new bucket key with partition
    now = datetime.now()
    month = now.month
    day = now.day
    
    formated_month = '{:02}'.format(month)
    formated_day = '{:02}'.format(day)
    
    raw_key = f"partitioned_data/{now.year}/{formated_month}/{formated_day}/{parquet_file_name}"

    # Fazendo upload do arquivo para o S3
    try:
        s3.upload_file(parquet_path, bucket_name, raw_key)
        print(f"File '{parquet_path}' successfully sent to bucket '{bucket_name}'")
    except FileNotFoundError:
        print(f"File '{parquet_path}' not found")
    except Exception as e:
        print(f"An error occurred while uploading to S3: {e}")


def convert_to_parquet(csv_path: str, parquet_path: str) -> None:
    print(f"Converting to parquet ...")

    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, index=False)

    print(f"Success to Converting file to parquet")

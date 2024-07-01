import boto3


def upload_file_to_s3(csv_path: str, csv_file_name: str, bucket_name: str) -> str:
    s3 = boto3.client("s3", region_name="us-east-1")

    # Fazendo upload do arquivo para o S3
    try:
        s3.upload_file(csv_path, bucket_name, csv_file_name)
        print(f"File '{csv_path}' successfully sent to bucket '{bucket_name}'")
    except FileNotFoundError:
        print(f"File '{csv_path}' not found")
    except Exception as e:
        print(f"An error occurred while uploading to S3: {e}")

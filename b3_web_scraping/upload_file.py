import boto3


def upload_file_to_s3(csv_path: str, csv_file_name: str, bucket_name: str) -> str:
    s3 = boto3.client("s3", region_name="us-east-1")

    # Fazendo upload do arquivo para o S3
    try:
        s3.upload_file(csv_path, bucket_name, csv_file_name)
        message = f"Arquivo '{csv_path}' enviado com sucesso para o bucket '{bucket_name}'"
    except FileNotFoundError:
        message = f"Arquivo '{csv_path}' não encontrado"
    except Exception as e:
        message = f"Ocorreu um erro durante o upload para o S3: {e}"
    finally:
        return message

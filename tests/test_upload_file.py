from b3_web_scraping import upload_file

def test_upload_file_to_s3():
    csv_path = "test_dados_b3.csv"
    bucket_name = "b3-raw"
    csv_file_name = "test_dados_b3.csv"
    
    message = upload_file.upload_file_to_s3(
        csv_path = csv_path, csv_file_name = csv_file_name, bucket_name = bucket_name
    )
    
    assert message == f"Arquivo '{csv_path}' enviado com sucesso para o bucket '{bucket_name}'" 
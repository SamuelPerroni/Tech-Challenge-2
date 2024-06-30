from b3_web_scraping import upload_file, web_scraping
from constantes import B3_URL, BUCKET_NAME, CSV_FILE_NAME, CSV_PATH

if __name__ == "__main__":
    # Realiza a etapa de raspagem de dados no site do b3 e gera um arquivo .csv
    web_scraping.get_values_b3(url=B3_URL, csv_path=CSV_PATH)
    
    # Coleta o arquivo gerado no scraping e sobe para o bucket raw
    upload_file.upload_file_to_s3(
        csv_path=CSV_PATH, csv_file_name=CSV_FILE_NAME, bucket_name=BUCKET_NAME
    )

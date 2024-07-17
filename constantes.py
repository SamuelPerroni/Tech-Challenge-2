import os

B3_URL = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
CSV_FILE_NAME = f"b3_data.csv"
CSV_PATH = os.path.join("output_file", CSV_FILE_NAME)
BUCKET_NAME_RAW = "b3-raw"
BUCKET_NAME_CLEANSED = "b3-cleansed"

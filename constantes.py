import os
from datetime import datetime

B3_URL = 'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'
CSV_FILE_NAME = f'dados_b3_{datetime.now().strftime('%d%m%Y')}.csv'
CSV_PATH = os.path.join('output_file', CSV_FILE_NAME)
BUCKET_NAME = 'b3-raw'

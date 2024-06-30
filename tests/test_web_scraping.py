from b3_web_scraping import web_scraping
import os

def test_web_scraping_b3():
    url = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
    csv_path = "test_dados_b3.csv"
    
    web_scraping.get_values_b3(url, csv_path)
    
    file_exists = os.path.exists(csv_path)
    if file_exists:
        os.remove(csv_path)
    
    assert file_exists

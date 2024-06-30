import time
from io import StringIO

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)


def get_values_b3(url: str, csv_path: str) -> None:
    try:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "table.table.table-responsive-sm.table-responsive-md")
            )
        )

        all_data = []

        while True:
            table = driver.find_element(
                By.CSS_SELECTOR, "table.table.table-responsive-sm.table-responsive-md"
            )
            table_html = table.get_attribute("outerHTML")
            df = pd.read_html(StringIO(table_html))[0]
            df = df.iloc[:-2]

            all_data.append(df)

            try:
                next_button = driver.find_element(
                    By.XPATH,
                    '//*[@id="listing_pagination"]/pagination-template/ul/li[8]/a',
                )
                next_button.click()
                time.sleep(1)

            except Exception as e:
                print(
                    f"Não foi possível encontrar o botão de próxima página ou ocorreu um erro: {e}"
                )
                break

        if all_data:
            final_df = pd.concat(all_data, ignore_index=True)
            print(final_df.head())
            final_df.to_csv(csv_path, index=False)

    finally:
        driver.quit()

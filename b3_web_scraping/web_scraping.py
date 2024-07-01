from io import StringIO

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# install and initialize chrome driver
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)


def get_values_b3(url: str, csv_path: str) -> None:
    """
    get values from b3 daily information and generate a csv file from DataFrame

    Parameters:
        url (str): b3 webpage URL
        csv_path (str): csv filepath to store data
    """
    print("get_values_b3 is started ...")

    try:
        # Access b3 website to Scrap the data
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "table.table.table-responsive-sm.table-responsive-md")
            )
        )

        all_data = []

        while True:
            """
            Iterates through all available table pages,
            collecting the data and adding it to a list of DataFrames
            """
            table = driver.find_element(
                By.CSS_SELECTOR, "table.table.table-responsive-sm.table-responsive-md"
            )
            table_html = table.get_attribute("outerHTML")
            df = pd.read_html(StringIO(table_html))[0]
            df = df.iloc[:-2]

            all_data.append(df)

            try:
                element_exists = check_exists_by_xpath(
                    '//*[@id="listing_pagination"]/pagination-template/ul/li[8]/a'
                )

                if element_exists:
                    next_button = driver.find_element(
                        By.XPATH,
                        '//*[@id="listing_pagination"]/pagination-template/ul/li[8]/a',
                    )
                    next_button.click()

                else:
                    print(
                        "There is no more page available in the table, writing data to csv..."
                    )
                    break

            except Exception as e:
                print(f"An error occurred during execution: {e}")
                all_data.clear()
                break

        if all_data:
            # Concatenates the list of DataFrames into a single one and saves it in a .csv
            final_df = pd.concat(all_data, ignore_index=True)
            final_df.to_csv(csv_path, index=False)

    finally:
        driver.quit()


def check_exists_by_xpath(xpath: str) -> bool:
    """
    Check if element exists and returns a boolean value

    Argument:
        xpath (str): xpath of the HTML element to be identified

    Returns:
        bool: True if element exists, False otherwise
    """
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

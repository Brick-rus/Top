"""Файл с конфигурационными данными для тестов"""

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=3') # Скрываем назящие Third party cookie
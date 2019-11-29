import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/wait2.html'

with webdriver.Firefox() as driver:
    driver.get(link)
    button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()

    message = driver.find_element_by_id('verify_message')

    assert "successful" in message.text

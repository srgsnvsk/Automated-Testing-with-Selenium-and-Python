# решение задачи
# вариант 2

import math

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    browser.find_element(
        By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000))
    ).click()
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    browser.quit()

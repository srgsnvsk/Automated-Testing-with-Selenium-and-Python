# теория
# скрипт скроллит страницу на заданное количество пикселей

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
time.sleep(1)
browser.execute_script("window.scrollBy(0, 100);")
time.sleep(2)
button.click()

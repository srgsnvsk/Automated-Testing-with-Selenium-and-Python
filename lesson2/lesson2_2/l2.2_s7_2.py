# теория

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
time.sleep(1)
element.send_keys(file_path)
time.sleep(1)

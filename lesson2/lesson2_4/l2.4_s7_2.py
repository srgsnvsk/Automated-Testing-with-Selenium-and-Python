# теория

from selenium.webdriver.common.by import By

# класс явных ожиданий используется совместно с expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

# инструмент явного ожидания
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
button.click()
message = browser.find_element(By.ID, "verify_message")

# проверяем, что в тексте сообщения содержится Verification was successful!
assert "Verification was successful!" in message.text

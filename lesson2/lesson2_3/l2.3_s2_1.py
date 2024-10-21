# теория
# принимаем alert

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://example.com")

# выполняем JavaScript для вызова alert
browser.execute_script("alert('Hello, world!');")

# ждем, чтобы увидеть закрытие alert
time.sleep(2)

# переключаемся на активный alert
alert = browser.switch_to.alert
# извлекаем текст из alert
alert_text = alert.text
# выводим текст из alert в консоль
print("Текст в alert:", alert_text)
# принимаем alert
alert.accept()

# ждем, чтобы увидеть закрытие alert
time.sleep(2)

# Закрываем браузер
browser.quit()

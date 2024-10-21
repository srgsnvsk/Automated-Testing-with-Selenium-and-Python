# теория
# вводим текст и принимаем prompt

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://example.com")

# Выполняем JavaScript для вызова prompt
browser.execute_script("prompt('Вы согласны учиться дальше?');")

# ждем, чтобы увидеть закрытие prompt
time.sleep(2)

# переключаемся на активный prompt
prompt = browser.switch_to.alert
# извлекаем текст в prompt
prompt_text = prompt.text
# выводим текст из prompt в консоль
print("Текст в prompt:", prompt_text)
# вводим текст в prompt
prompt.send_keys("Да!")

time.sleep(4)

# принимаем prompt
prompt.accept()

# ждем, чтобы увидеть закрытие prompt
time.sleep(2)

# Закрываем браузер
browser.quit()

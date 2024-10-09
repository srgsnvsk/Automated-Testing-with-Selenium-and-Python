# теория
# отклоняем confirm

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://example.com")

# выполняем JavaScript для вызова confirm
browser.execute_script("confirm('Вы согласны учиться дальше?');")

# ждем, чтобы увидеть закрытие confirm
time.sleep(2)

# переключаемся на активный confirm
confirm = browser.switch_to.alert
# извлекаем текст из confirm
confirm_text = confirm.text
# выводим текст из confirm в консоль
print("Текст в confirm:", confirm_text)
# отклоняем confirm
confirm.dismiss()

# ждем, чтобы увидеть закрытие confirm
time.sleep(2)

# Закрываем браузер
browser.quit()

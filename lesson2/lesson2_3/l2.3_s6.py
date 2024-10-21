# решение задачи

import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


# рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # жмакаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()

    # переключение на новую вкладку браузера
    browser.switch_to.window(browser.window_handles[1])

    # подхватываем значение х
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # заполняем поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(
        str(math.log(abs(12 * math.sin(int(x)))))
    )

    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    # копируем из алерта число для ответа
    alert = browser.switch_to.alert
    print("Проверочный код: ", alert.text.split()[-1])
    alert.accept()

finally:
    # ожидание
    time.sleep(2)
    # закрытие браузера
    browser.quit()

# пустая строка

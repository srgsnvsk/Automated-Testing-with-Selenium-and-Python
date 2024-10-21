# решение задачи

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# рассчет значения функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# вывод проверочного кода в консоль
def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print("Проверочный код: ", alert.text.split()[-1])
    alert.accept()


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим сундук и берем значение valuex
    find_img = browser.find_element(By.ID, "treasure")
    valuex = find_img.get_attribute("valuex")
    print("valuex: ", valuex)
    assert valuex is not None, "Нету valuex"

    # вычисляем по формуле
    calculate = calc(valuex)

    # вставляем наше вычисление
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(calculate)

    # отмечаем чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    # отмечаем радиобаттон
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # выводим проверочный код
    print_answer(browser)

finally:
    # ожидание для наглядности
    time.sleep(2)
    # закрываем браузер
    browser.quit()

# не забываем оставить пустую строку в конце файла

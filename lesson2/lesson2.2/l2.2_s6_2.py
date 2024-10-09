# решение задачи
# вариант: повыпендрежнее 1

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# вывод проверочного кода в консоль
def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print("Проверочный код: ", alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # подхватываем значение х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # заполняем поле
    answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # скроллим
    browser.execute_script("window.scrollBy(0, 150);")

    # отмечаем чекбокс
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    # отмечаем радиобаттон
    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    # выводим в консоль расчет функции
    print("Расчет математической функции:", y)

    # выводим проверочный код
    print_answer(browser)

finally:
    # ожидание
    time.sleep(2)
    # закрываем браузер
    browser.quit()

# пустая строка

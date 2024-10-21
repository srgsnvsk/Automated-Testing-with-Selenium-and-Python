# решение задачи
# вариант: лаконичный

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # подхватываем значение х
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # заполняем поле
    answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(
        str(math.log(abs(12 * math.sin(int(x)))))
    )

    # скроллим
    browser.execute_script("window.scrollBy(0, 150);")

    # отмечаем чекбокс
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    # отмечаем радиобаттон
    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    # выводим проверочный код
    alert = browser.switch_to.alert
    print("Проверочный код: ", alert.text.split()[-1])
    alert.accept()

finally:
    # ожидание
    time.sleep(2)
    # закрываем браузер
    browser.quit()

# пустая строка

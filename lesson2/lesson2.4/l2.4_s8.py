# решение задачи

import time  # паузы
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # находим кнопку book
    btn_book = browser.find_element(By.ID, "book").click()

    # скролл
    browser.execute_script("window.scrollBy(0, 100);")

    # подхватываем значение х и преобразуем в текст
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # заполняем поле и считаем функцию
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x_element))

    # нажимаем submit
    btn_solve = browser.find_element(By.CSS_SELECTOR, "#solve").click()

    # копируем из алерта число для ответа
    alert = browser.switch_to.alert
    print("Проверочный код:", browser.switch_to.alert.text.split()[-1])
    alert.accept()

finally:
    # ожидание
    time.sleep(5)
    # закрытие браузера
    browser.quit()

# пустая строка

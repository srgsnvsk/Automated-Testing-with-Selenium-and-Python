# решение задачи

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# вывод проверочного кода в консоль
def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print("Проверочный код: ", alert.text.split()[-1])
    alert.accept()


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элементы num1, num2 и забираем их текстовые значения
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text

    # считаем сумму преобразовав str в int и обратно в str
    sum = str(int(num1) + int(num2))

    # выводим в консоль числа и сумму
    print("Число 1: ", num1)
    print("Число 2: ", num2)
    print("Сумма: ", sum)

    # находим выпадающий список и выбираем значение равное сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    # нажимаем submit
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    # выводим проверочный код
    print_answer(browser)

finally:
    # ожидание для наглядности
    time.sleep(2)
    # закрытие браузера
    browser.quit()

# пустая строка

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
    link = "http://suninjuly.github.io/selects1.html"  # ссылка
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элементы num1, num2 и забираем их текстовые значения
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    get_num1 = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    get_num2 = num2.text

    # преобразуем str в int
    int_num1, int_num2 = int(get_num1), int(get_num2)

    # считаем сумму
    sum = int_num1 + int_num2

    # преобразуем int в str
    sum = str(sum)

    # выводим в консоль числа и сумму
    print("Число 1: ", get_num1)
    print("Число 2: ", get_num2)
    print("Сумма: ", sum)

    # находим выпадающий список и выбираем значение равное сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # выводим проверочный код
    print_answer(browser)

finally:
    # ожидание для наглядности
    time.sleep(2)
    # закрытие браузера
    browser.quit()

# пустая строка

# решение задачи

import time # паузы
import os # модуль для работы с ОС

from selenium import webdriver # webdriver набор команд управления браузером
from selenium.webdriver.common.by import By # класс By способ поиска элемента

# конструкция try/finnaly для закрытия браузера если тест упадет с ошибкой
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # фамилия
    f_name = browser.find_element(By.CSS_SELECTOR, f'input[placeholder="{'Enter first name'}"]').send_keys("Торвальдс")
    # имя
    l_name = browser.find_element(By.CSS_SELECTOR, f'input[placeholder="{'Enter last name'}"]').send_keys("Линус")
    # почта
    mail = browser.find_element(By.CSS_SELECTOR, f'input[placeholder="{'Enter email'}"]').send_keys("example@mail.com")
    
    file = browser.find_element(By.CSS_SELECTOR, "#file")

    # загружаем файл с пекарни
    # получаем путь к директории текущего исполняемого файла и добавляем к этому пути имя файла
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "file.txt")
    file.send_keys(file_path)
    
    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    # копируем из алерта число для ответа
    print("Проверочный код: ", browser.switch_to.alert.text.split()[-1])
    browser.switch_to.alert.accept()

finally:
    # ожидание
    time.sleep(2)
    # закрытие браузера
    browser.quit()

# пустая строка

# теория

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # <input class="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

    people_radio = browser.find_element(By.ID, "peopleRule")

    print(people_radio.get_attribute("name"))
    # Напечатает ruler, т.е. текстовое значение аттрибута

    print(people_radio.get_attribute("checked"))
    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

    print(people_radio.get_attribute("href"))
    # Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.

finally:
    # ожидание для наглядности
    time.sleep(2)
    # закрываем браузер
    browser.quit()

# пустая строка в конце файла

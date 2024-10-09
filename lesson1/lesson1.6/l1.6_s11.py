# решение задачи

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR, "input.form-control.second[placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")
    input3 = browser.find_element(
        By.CSS_SELECTOR, "input.form-control.third[placeholder='Input your email']"
    )
    input3.send_keys("example@example.com")
    input4 = browser.find_element(
        By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your phone:']"
    )
    input4.send_keys("8-800-555-55-55")
    input5 = browser.find_element(
        By.CSS_SELECTOR, "input.form-control.second[placeholder='Input your address:']"
    )
    input5.send_keys("Kursk")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    # закрываем браузер
    browser.quit()

# пустая строка в конце файла

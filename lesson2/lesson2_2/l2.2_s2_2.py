# теория
# ищем элемент по value

from selenium import webdriver
from selenium.webdriver.common.by import By

# класс Select для работы с выпадающими списками
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")  # ищем элемент с текстом "1"

# пустая строка

# теория
# переход по вкладкам

from selenium import webdriver
import time

# Инициализация браузера
browser = webdriver.Chrome()

# Открываем первую вкладку
browser.get("https://www.example.com")

# Открываем новую вкладку
browser.execute_script("window.open('https://www.bing.com', '_blank');")

# Получаем список всех открытых вкладок/окон
window_handles = browser.window_handles
print("Список всех открытых вкладок: ", window_handles)

# Переключаемся на вторую вкладку (новую)
browser.switch_to.window(window_handles[1])

# Делаем какие-то действия на новой вкладке
time.sleep(2)
print("На новой вкладке:", browser.current_url)

# Переключаемся обратно на первую вкладку
browser.switch_to.window(window_handles[0])

# Проверяем URL первой вкладки
print("Вернулись на первую вкладку:", browser.current_url)

# Закрываем браузер
browser.quit()

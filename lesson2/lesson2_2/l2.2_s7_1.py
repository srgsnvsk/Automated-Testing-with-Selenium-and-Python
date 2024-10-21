# теория

import os

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
print("\033[32mДиректория с исполняемым файлом:\033[0m", current_dir)
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, "file.txt")
print("\033[32mПуть к файлу который хотим загрузить:\033[0m", file_path)
# загрузка файла
# element.send_keys(file_path)

import os

folder_name = str(input('Введите название папки для удаления:'))
if os.path.exists(folder_name):
    os.rmdir(folder_name)
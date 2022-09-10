import os

name1 =input('Введите название папки для удаления:')
if os.path.exists(f'name1'):
    os.rmdir(f'name1')
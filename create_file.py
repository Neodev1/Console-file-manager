import os

def create_folder():
    new_folder = str(input('Введите название папки:'))
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
create_folder()



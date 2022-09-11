import os

def is_folder():
    if os.path.isdir('.')==True:
        print(os.listdir())
is_folder()

# мне кажется код неправильный. Он выводит и папки и файлы. Подскажите как правильно?
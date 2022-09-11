import os

def is_file():
    if os.path.isfile('.')==True:
        print(os.listdir())
is_file()

# мне кажется код неправильный. Он выводит и папки и файлы. Подскажите как правильно?
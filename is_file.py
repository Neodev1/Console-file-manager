import os

def is_file():
    if os.path.isfile('.')==True:
        print(os.listdir())
is_file()
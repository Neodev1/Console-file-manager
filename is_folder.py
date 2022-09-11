import os

def is_folder():
    if os.path.isdir('.')==True:
        print(os.listdir())
is_folder()
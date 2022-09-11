import random


def get_random_person():
    """
    Получить 1 го случайного человека
    :return:
    """
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Д.И.Менделеева': '08.02.1834',
                     'Леонардо Да Винчи': '15.04.1452', 'Адриано Челентано': '06.01.1938',
                     'Джим Кэрри': '17.01.1962', 'Джекки Чан': '07.04.1954',
                     'Киану Ривз': '02.09.1964'}

    # print(FAMOUS_PEOPLE)
    # print(FAMOUS_PEOPLE.items())
    name, date = random.choice(list(FAMOUS_PEOPLE.items()))
    return name, date


def get_person_and_question():
    # Выбираем случайного человека
    name, date = get_random_person()

    # Спрашиваем когда он родился
    answer = input(f'Когда родился {name} ')

    # Если введенный год совпадает с правильным
    if answer == date:
        print('Верно')
    else:
        print('Неверно')


# print('__name__', __name__)
if __name__ == '__main__':
    print('Проверка фукцнии', get_random_person())

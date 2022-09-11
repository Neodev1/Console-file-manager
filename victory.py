
# 1. Импорт конкретных функций из модуля
# from <название модуля> import нужные функций через ,
from famous_persons_mdl import get_random_person, get_person_and_question

rounds = int(input('Сколько раз вы хотите играть?'))

for i in range(rounds):
    get_person_and_question()

print('Пока!')
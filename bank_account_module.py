balance=0
history=[]

def purchase(balance):
    cost=int(input('Введите сумму покупки'))
    if cost > balance:
        print('Недостаточно средств')
    else:
        balance -= cost
        name=input('Введите название покупки')
        history.append((name, cost))
    return balance

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Ваш счет {balance}')


    choice = input('Выберите пункт меню')
    if choice == '1':
        money=int(input('Введите сумму'))
        balance += money
    elif choice == '2':
        balance = purchase(balance)
    elif choice == '3':
        print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
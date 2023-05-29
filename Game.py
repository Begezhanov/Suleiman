from random import randint
print('\nКамень-ножницы-бумага!')
print('Вы будете играть с компьютером в "су-ли-фа".')
print('Играем до трех побед!!!\n')
print('1---Камень \n2---Ножницы \n3---Бумага \n')

cnt_pc = 0
cnt_player = 0

while True:
    x = randint(1, 3)
    
    print('-----' * 7)
    print('Компьютер уже сделал свой выбор!')
    print('Теперь ваша очередь...\n')
    
    choice = int(input('Сделайте свой выбор: '))
    print()
    if choice < 1 or choice > 3:         
        print('Вы сделали не правильный выбор, он должен быть в пределах от 1-го до 3-х!!!')
        answer = input('Продолжаем (Да/Нет)? ')
        if answer in 'ДАдаДадА':
            continue
        elif answer in 'НЕТнетНетнЕтнЕТнеТНЕт':
            print('Game over!')
            break
        else: 
            print('error')
        break
    if x == 1:
            x = 'Камень'
    elif x == 2:
            x = 'Ножницы'
    elif x == 3:
            x = 'Бумага'
    if choice == 1:
            choice = 'Камень'
    elif choice == 2:
            choice = 'Ножницы'
    elif choice == 3:
            choice = 'Бумага'

    print('Выбор компьютера: ', x)
    print('Ваш выбор: ', choice)

    if choice == x:
        print('НИЧЬЯ!!!')

    elif choice == 'Камень' and x == 'Ножницы':
        cnt_player += 1
    elif choice == 'Бумага' and x == 'Камень':
        cnt_player += 1
    elif choice == 'Ножницы' and x == 'Бумага':
        cnt_player += 1
    elif choice == 'Камень' and x == 'Бумага':
        cnt_pc += 1
    elif choice == 'Ножницы' and x == 'Камень':
        cnt_pc += 1
    elif choice == 'Бумага' and x == 'Ножницы':
        cnt_pc += 1
    
    print('Счет(Компьютер: ' + str(cnt_pc) + ', Человек: ' + str(cnt_player) + ')\n')

    if cnt_pc == 3:
        print('Победил компьютер :(((')
        break
    elif cnt_player == 3 and cnt_pc == 0:
        print('Тотальная победа ЧЕЛОВЕЧЕСТВА!!!')
        break
    elif cnt_player == 3:
        print('Победил человек, поздравляю Вас!!!')
        break
first = int(input('Необходимо ввести 3 числа. Введите первое: '))
second = int(input('Теперь введите второе число: '))
third = int(input('и третье число: '))
if first == second == third:
    print ('Количество введённых чисел, равных между собой: 3')
elif first == second or second ==  third or first == third:
    print('Количество введённых чисел, равных между собой: 2')
else:
    print('Количество введённых чисел, равных между собой: 0, вы ввели 3 разных числа')
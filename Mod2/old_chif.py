import random
def solving_case(number_in):
    password = []
    summ = 0
    for number1 in range(1,21):
        for number2 in range(1,21):
            if number2 < number1: # исключаем повторы
                continue
            if number1 == number2: # исключаем не нужные значения
                continue
            summ = number1+number2
            if number_in >= summ:
                if number_in % summ == 0:
                    password.append([number1, number2])# заполняем список значениями в соответствии с условием задачи
                else:
                    continue
            else:
                break
    return password
# number_in = int(input('введите число: ')) # число с клавиатуры
# print ('Ваше число:', number_in, '\n', 'для решения загадки нужно ввести справа: ', solving_case(number_in)) # проверка работы функции на конкретном числе
number_in_left_side = [] # список, который будет заполнен числами от 3 до 20
for i in range (3,21):
    number_in_left_side.append(i)
num = random.choice(number_in_left_side)# выбираем случайное число от 3 до 20
#print ('на левой стороне выпал номер: ', num, '\n', 'для решения загадки нужно ввести справа: ', solving_case(num)) # проверка работы функции до вывода результата
output = str(solving_case(num)) # изменяем тип данных, чтобы скорректировать вывод
output = output.replace('[', '')
output = output.replace(']', '')
output = output.replace(', ', '')
print ('на левой стороне выпал номер: ', num, '\n', 'для решения загадки нужно ввести справа: ', output)
summ = 0
def is_dict(not_list):
    """
    Функция для работы со словарями
    """
    global summ
    keys = [*not_list]
    for i in range(len(keys)):
        # проходимся по ключам, рассматривая как строчные, так и численные значения
        if type(keys[i]) == str:
            summ += len(keys[i])
        elif (type(keys[i]) == int
              or type(keys[i]) == float
              or type(keys[i]) == bool):
            summ += int(keys[i])
        if (type(not_list[keys[i]]) == int
                # затем проходимся по значениям, рассматривая как строчные, так и численные значения
                or type(not_list[keys[i]]) == float
                or type(not_list[keys[i]]) == bool):
            summ += int(not_list[keys[i]])
        elif type(not_list[keys[i]]) == str:
            summ += len(not_list[keys[i]])
def Calculate_all(listing):
    """
        Основная рекурсивная функция для подсчёта
        суммы чисел и длинны строк
    """
    global summ
    temp=0
    if type(listing) != dict:
        for i in range(len(listing)):
            # рассматриваем списки и кортежи
            if (type(listing[i]) == list
                    or type(listing[i]) == tuple):
                for j in range(len(listing[i])):
                    if (type(listing[i][j]) == int
                            or type(listing[i][j]) == float
                            or type(listing[i][j]) == bool):
                        summ += int(listing[i][j])
                    elif type(listing[i][j]) == str:
                        summ += len(listing[i][j])
                    elif type(listing[i][j]) == dict:
                        is_dict(listing[i][j])
                    else:# вызов рекурсии, для работы со сложным куском "[{(2, 'Urban', ('Urban2', 35))}]" или подобными
                        if any(listing[i][j]) != False:
                            Calculate_all(listing[i][j])
            elif type(listing[i]) == dict:
                is_dict(listing[i])
            elif type(listing[i]) == str:
                summ += len(listing[i])
            elif (type(listing[i]) == int
                  or type(listing[i]) == float
                  or type(listing[i]) == bool):
                summ += int(listing[i])
            elif type(listing[i]) == set:
                # для работы со множествами используем временную переменную и обращаемся к рекурсии
                temp = list(listing[i])
                Calculate_all(temp)
    else:
        is_dict(listing)
    return summ
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print('Сумма всех чисел и длинны всех строк в исходном фрагменте данных равна -', Calculate_all(data_structure))
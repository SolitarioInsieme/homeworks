def get_matrix(n, m, value):
    matrix = []
    for i in range(n): # добавляем строки в нашу матрицу
        column = []
        for j in range (m): # записываем значения по количеству колонн в матрице
            column.append (value)
        matrix.append(column)
    print ('Ваша матрица: \n') # вносим ясности в вывод
    for a in range(n):
        print (matrix[a], '\n') # выводим матрицу так, как она должна выглядеть на бумаге)
    return matrix
result1 = get_matrix(2, 2, 10)
print ('Та же матрица, в строку: ', result1, '\n')
result2 = get_matrix(3, 5, 42)
print ('Та же матрица, в строку: ', result2, '\n')
result3 = get_matrix(4, 2, 13)
print ('Та же матрица, в строку: ', result3, '\n')
# дополнил выводом в виде матрицы, решил так же вывести как было в задании
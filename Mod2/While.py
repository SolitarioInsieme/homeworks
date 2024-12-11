my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
current_number = 0
print ('Выводим в консоль положительные числа:')
while True:
    if len(my_list) == current_number:
        print ('Список закончился, выводить нечего')
        break
    elif my_list[current_number] > 0:
        print (my_list[current_number])
        current_number = current_number + 1
        continue
    elif my_list[current_number] == 0:
        current_number = current_number + 1
        continue
    # else:  #данным условием проверял, что будет если дойти до конца цикла
    #     print(my_list[current_number])
    #     current_number = current_number + 1
    else:
        print ('следующие число - отрицательное, выполнение цикла окончено')
        break


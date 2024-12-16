numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True  # переменная для проверки на простоту числа

for i in range(len(numbers)): #
    if numbers[i] == 1:  # пропускаем 1, т.к. это ни простое, ни составное число
        continue
    else:
        for j in range(2, numbers[i]): # цикл проверяет является ли число простым,
            # по средствам деления его на числа от 2 до предыдущего числа
            if numbers[i] % j == 0:
                is_prime = False
                break
            else:
                continue
        if not is_prime: # если число не прошло проверку, записываем его в список не простых чисел
            not_primes.append(numbers[i])
            is_prime = True
        else: # в ином случае записываем его в список простых
            primes.append(numbers[i])
print('Простые числа: ', primes)
print('Составные числа: ', not_primes)

import fake_math as fake
import true_math as true

result1 = fake.divide_fake(369, 3)
result2 = fake.divide_fake(10, 0)
result3 = true.divide_true(749, 7)
result4 = true.divide_true(20, 0)
print ('Результат деления первый, при использовании fake-функции:', result1)
print ('Результат деления второй, при использовании fake-функции:', result2)
print ('Результат деления первый, при использовании true-функции:', result3)
print ('Результат деления второй, при использовании true-функции:', result4)
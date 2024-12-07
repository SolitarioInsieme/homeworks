my_dict = {'Viktor' : 2000, 'Misha' : 2002, 'Masha' : 2007, 'Danil' : 2012}
print('Словарь с годами рождения: ', my_dict)
print('Значение по существующему ключу: ', my_dict.get('Masha'))
print('Значение по новому ключу: ', my_dict.get('Oleg'))
my_dict.update({'Natasha' : 1984,
               'Aphanasiy' : 1974})
print('Значение удаленной пары: ', my_dict.pop('Viktor'))
print('Словарь после изменений: ', my_dict)
my_set = {11, 27, 94, 27, 32, 395, 94, 11, 'Арбуз, Арбуз'}
print('Множество до изменений: ', my_set)
my_set.add(True)
my_set.add((56, 37, 94, 975))
my_set.remove(11)
print('Множество после изменений: ', my_set)
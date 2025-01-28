class House:
    houses_history = []
    __instance = None
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, name, number_of_floors):
         self.name = name
         self.number_of_floors = int(number_of_floors)
    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if self.number_of_floors >= new_floor >= 1:
            for i in range(new_floor+1):
                print(f'вы на этаже {i} дома "{self.name}"')
                if i == new_floor:
                    print('Вы достигли нужного этажа')
        else:
            print(f'Такого этажа не существует в доме "{self.name}"')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Неверный тип данных'
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Неверный тип данных'
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Неверный тип данных'
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Неверный тип данных'
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Неверный тип данных'
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Неверный тип данных'
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            print(f'В доме {self.name} теперь {self.number_of_floors} этажей')
            return self
        else:
            return 'Неверный тип данных'
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            print(f'В доме {self.name} теперь {self.number_of_floors} этажей')
            return self
        else:
            return 'Неверный тип данных'
    def __radd__(self, value):
        if isinstance(value, int):
            temp = self.number_of_floors
            self.number_of_floors = value + self.number_of_floors
            print(f'В доме {self.name} теперь {self.number_of_floors} этажей')
            return self
        else:
            return 'Неверный тип данных'
    def __del__(cls):
        print( f'{cls.name} снесён, но он останется в истории')
house1 = House('ЖК Голубево', 18)
print(House.houses_history)
house2 = House('ЖК Малиновка', 5)
print(House.houses_history)
house3 = House('Загородный домик у моря', 2)
print(House.houses_history)
house1.go_to(10)
house2.go_to(4)
house3.go_to(4)
print("_________________________________________________________________________________________")
print(house1)
print(house2)
print(house3)
print(len(house1))
print(len(house2))
print(len(house3))
print("_________________________________________________________________________________________")
print(house1 == house2)
print(house1 > house3)
print(house2 < house3)
print(house1 >= house2)
print(house3 <= house2)
print(house2 != house3)

house1 = house1 + 10
print(house1)
house2 += 5
print(house2)
house3 = 3 + house3
print(house3)
print("_________________________________________________________________________________________")
del house1
del house2
print(House.houses_history)
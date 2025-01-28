class House:
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
house1 = House('ЖК Голубево', 18)
house2 = House('ЖК Малиновка', 5)
house3 = House('Загородный домик у моря', 2)
house1.go_to(10)
house2.go_to(4)
house3.go_to(4)
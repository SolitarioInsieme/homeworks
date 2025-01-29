class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Приветствую, выберите действие: \n1 - Вход\n2 - Регистрация\n")
        if choice == "1": #Алгоритм входа
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choice == "2": # Алгоритм регистрации
            user = User(input("Введите логин: "),
                        password := input("Введите пароль: "),
                        re_password := input("Повторите пароль: "))
            print('Пользователь успешно создан')
            if password != re_password:
                print('Пароли не совпадают, попробуйте ещё раз')
                continue
            database.add_user(user.username, user.password)
        else:
            print('Для выбора последующего действия необходимо ввести "1" или "2", попробуйте ещё раз')
            continue
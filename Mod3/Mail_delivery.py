def email_checker (mail):
    checker1 = False
    checker2 = False
    for i in range(len(mail)):
        if mail[i] == '@':
            checker1 = True
            break
    if (mail[len(mail) - 1] == 'm'
            and mail[len(mail) - 2] == 'o'
            and mail[len(mail) - 3] == 'c'
            and mail[len(mail) - 4] == '.'):
        checker2 = True
    elif (mail[len(mail) - 1] == 't'
          and mail[len(mail) - 2] == 'e'
          and mail[len(mail) - 3] == 'n'
          and mail[len(mail) - 4] == '.'):
        checker2 = True
    elif (mail[len(mail) - 1] == 'u'
        and mail[len(mail) - 2] == 'r'
        and mail[len(mail) - 3] == '.'):
        checker2 = True
    if checker1 == checker2 == True:
        return True
    return False
def send_email (message, recipient,*, sender = 'university.help@gmail.com'):
    if not email_checker(recipient):
        print ('Невозможно отправить письмо с адреса ', sender,
               'на адрес ', recipient, '\t', 'Не верно указан адрес получателя!')
        return
    if not email_checker(sender):
        print('Невозможно отправить письмо с адреса ', sender,
              'на адрес ', recipient, '\t', 'Не верно указан адрес отправителя!')
        return
    if recipient == sender:
        print ('Нельзя отправить письмо самому себе!')
        return
    elif sender == 'university.help@gmail.com':
        print ('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
        return
    print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
    return
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
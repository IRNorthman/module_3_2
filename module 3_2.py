def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    R1 = recipient.endswith(".com")
    R2 = recipient.endswith(".ru")
    R3 = recipient.endswith(".net")
    R4 = sender.endswith(".com")
    R5 = sender.endswith(".ru")
    R6 = sender.endswith(".net")
    if ("@" not in recipient) or ("@" not in sender) or (R1 == False and R2 == False and R3 == False) or (R4 == False and R5 == False and R6 == False):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print ("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print (f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
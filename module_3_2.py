recipient_1 = input('Введите email для получения сообщения - ')
message_1 = input('Введите текст сообщения - ')
dom_en = ['.com', '.ru', '.net']
var_recipient = False
sender_1 = input('Если желаете отправить письмо с другого адреса, то введите email отправителя - ')


if sender_1 != '':
    for i in range(len(dom_en)):  # проверяем правильность введенного Нестандартного email адреса
        if '@' in sender_1 and dom_en[i] in sender_1:
            break
        else: input('Введите правильный email отправителя - ')



def send_email(message, recipient, *, sender='university.help@gmail.com'):
    global var_recipient
    for i in range(len(dom_en)):  # проверяем правильность введенного email адреса
        if '@' in recipient and dom_en[i] in recipient:
            var_recipient = True
            break
        else:
            continue

    if var_recipient == False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе')

    elif sender == 'university.help@gmail.com' and sender != sender_1:
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient,'Текст письма : ',message_1)

    elif sender == 'university.help@gmail.com' and sender == sender_1:
        print('Вы выбрали отправителя по умолчанию')
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient,'Текст письма : ',message_1)

    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!!!, Письмо отправлено с адреса', sender, 'на адрес', recipient,'Текст письма : ',message_1)


if sender_1 == '':
    send_email(message_1, recipient_1)
else:
    send_email(message_1, recipient_1, sender=sender_1)

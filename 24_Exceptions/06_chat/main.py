def write_chat(user, text):
    with open('chat.txt', 'a', encoding='utf-8') as chat_file:
        chat_file.write(f'{user}: {text}')
        chat_file.write('\n')


while True:
    user_name = input('Введите имя пользователя: ')
    next_action = input('Посмотреть текущий текст чата. - 0, Отправить сообщение - 1: ')
    if next_action == '0':
        with open('chat.txt', 'r', encoding='utf-8') as chat_read_file:
            print(chat_read_file.read())
    else:
        new_message = input('Введите сообщение: ')
        write_chat(user_name, new_message)

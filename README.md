# DarkChatAPI Python Client

Клиентская библиотека Python для взаимодействия с API DarkChat.

## Установка
Для установки последней версии напрямую с GitHub:
```bash
pip install git+https://github.com/Dark-Tehno/DarkChatAPI.git
```

## Использование

```python
from DarkChat.v1 import ws_chat, chats # или другие функции
from DarkChat.v1 import account

token, status_code = account.login("username", "password")

if status_code == 200:
    chats_list, chats_status_code = chats(token)
    if chats_status_code == 200:
        ids_chats = []
        for chat_info in chats_list:
            ids_chats.append(int(chat_info['id']))
            if chat_info['user1']['username'] == 'username': # Ваш username
                print(f'{chat_info["id"]}: {chat_info["user2"]["username"]}')
            elif chat_info['user2']['username'] == 'username': # Ваш username
                print(f'{chat_info["id"]}: {chat_info["user1"]["username"]}')
        id_chat = int(input("Введите id чата: "))
        if id_chat not in ids_chats:
            print('Такого чата нет')
            exit()
    else:
        print(f"Ошибка при получении чатов: {chats_status_code}")
        exit()

    # Подключение к WebSocket чата
    def my_message_handler(ws, message):
        print(f"Новое сообщение в чате: {message}")

    chat_connection = ws_chat(token=token, chat_id=id_chat, on_message_callback=my_message_handler)
    print("Подключено к WebSocket чата. Ожидание сообщений...")
    # Держите основной поток активным, чтобы WebSocket работал
    try:
        while True:
            pass # или input() для простого ожидания
    except KeyboardInterrupt:
        if chat_connection:
            chat_connection.close()
        print("Соединение закрыто.")
else:
    print(f"Ошибка при получении токена: {status_code}")
```

## Документация

Последняя версия документация доступна по адресу: [https://vsp210.ru/api/v2/](https://vsp210.ru/api/v2/)

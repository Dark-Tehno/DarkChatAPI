# DarkChatAPI Python Client

Клиентская библиотека Python для взаимодействия с API DarkChat.

## Установка
Для установки последней версии напрямую с GitHub:
```bash
pip install git+https://github.com/Dark-Tehno/DarkChatAPI.git
```

## Использование

```python
from DarkChat import chat, ws_chat 
from DarkChat import account
token = account.login("user", "password")

if token:
    # Подключение к WebSocket чата
    def my_message_handler(ws, message):
        print(f"Новое сообщение в чате: {message}")

    chat_connection = ws_chat(token="your_token_here", chat_id=1, on_message_callback=my_message_handler)
    print("Подключено к WebSocket чата. Ожидание сообщений...")
    # Держите основной поток активным, чтобы WebSocket работал
    try:
        while True:
            pass # или input() для простого ожидания
    except KeyboardInterrupt:
        if chat_connection:
            chat_connection.close()
        print("Соединение закрыто.")
```

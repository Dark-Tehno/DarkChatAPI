# d:\Dev\Python\project_34\testapi\API_DarkChat\DarkChat\__init__.py
from .chat import (
    BASE_URL,
    BASE_URL_WS,
    chats,
    chat,
    ws_online,
    ws_chat
)

from .account import (
    login,
    register,
    logout,
    my_data,
    user_data
)


__all__ = [
    'BASE_URL',
    'BASE_URL_WS',
    'chats',
    'chat',
    'ws_online',
    'ws_chat',
    'login',
    'register',
    'logout',
    'my_data',
    'user_data'
]

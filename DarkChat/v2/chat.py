import websocket
import threading
from urllib.parse import urlencode
from .utils import _api_request


BASE_URL = 'https://vsp210.ru/api/v2/'
BASE_URL_WS = 'wss://vsp210.ru/ws/'

def chats(token):
    url = f'{BASE_URL}chats/'
    headers = {'Authorization': f'Token {token}'}
    return _api_request('post', url, headers=headers)

def chat(token, chat_id):
    url = f'{BASE_URL}chat/{chat_id}/'
    headers = {'Authorization': f'Token {token}'}
    return _api_request('post', url, headers=headers)


# --- WebSocket Functionality ---

def _default_on_message(ws, message):
    print(f"WebSocket Message: {message}")

def _default_on_error(ws, error):
    print(f"WebSocket Error: {error}")

def _default_on_close(ws, close_status_code, close_msg):
    status_msg = f"WebSocket Closed: Status Code='{close_status_code}', Message='{close_msg}'"
    print(status_msg)

def _default_on_open(ws):
    print("WebSocket Opened")

def ws_online(token,
              on_open_callback=_default_on_open,
              on_message_callback=_default_on_message,
              on_error_callback=_default_on_error,
              on_close_callback=_default_on_close,
              enable_trace=False):
    """
    Connects to the online status WebSocket.
    Returns the WebSocketApp instance.
    """
    if enable_trace:
        websocket.enableTrace(True)
    params = urlencode({'token': token})
    ws_url = f"{BASE_URL_WS}online/?{params}"
    ws = websocket.WebSocketApp(ws_url,
                                on_open=on_open_callback,
                                on_message=on_message_callback,
                                on_error=on_error_callback,
                                on_close=on_close_callback)

    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.daemon = True  # Thread will exit when main program exits
    ws_thread.start()
    return ws

def ws_chat(token, chat_id,
            on_open_callback=_default_on_open,
            on_message_callback=_default_on_message,
            on_error_callback=_default_on_error,
            on_close_callback=_default_on_close,
            enable_trace=False):
    """
    Connects to a specific chat WebSocket.
    Returns the WebSocketApp instance.
    """
    if enable_trace:
        websocket.enableTrace(True)
    params = urlencode({'token': token})
    ws_url = f"{BASE_URL_WS}chat/{chat_id}/?{params}"
    ws = websocket.WebSocketApp(ws_url,
                                on_open=on_open_callback,
                                on_message=on_message_callback,
                                on_error=on_error_callback,
                                on_close=on_close_callback)
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.daemon = True
    ws_thread.start()
    return ws

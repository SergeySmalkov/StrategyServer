# python_server.py

import websocket
import threading

def on_message(ws, message):
    print(f"Received: {message}")
    # Here you can add logic to handle the fake data


def start_websocket_listener():
    ws = websocket.WebSocketApp("ws://localhost:9002/",
                                on_message=on_message)
    ws.run_forever()


if __name__ == "__main__":
    # Starting the WebSocket listener in a separate thread
    ws_thread = threading.Thread(target=start_websocket_listener)
    ws_thread.start()

    # Main thread logic (if any) can go here.
    try:
        while True:
            pass
    except KeyboardInterrupt:
        exit()


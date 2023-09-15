
import websocket
import threading
import zmq
import time
def on_message(ws, message):
    print(f"Received: {message}")
    # Here you can add logic to handle the fake data


def start_websocket_listener():
    ws = websocket.WebSocketApp("ws://localhost:9002/",
                                on_message=on_message)
    ws.run_forever()
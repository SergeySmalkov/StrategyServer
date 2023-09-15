
import websocket
import threading
import zmq
import time
import websocket_connection
from zmq_connection import zmq_accept_orders, zmq_send_order_updates

if __name__ == "__main__":
    # Starting the WebSocket listener in a separate thread
    ws_thread = threading.Thread(target=websocket_connection.start_websocket_listener)
    ws_thread.start()

    context = zmq.Context()

    zmq_order_listener = threading.Thread(target=zmq_accept_orders, args=(context,))
    zmq_order_updater = threading.Thread(target=zmq_send_order_updates, args=(context,))
    zmq_order_listener.start()
    zmq_order_updater.start()

    # Main thread logic (if any) can go here.
    try:
        while True:
            pass
    except KeyboardInterrupt:
        exit()


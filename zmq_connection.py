import zmq
import threading

def zmq_accept_orders(context):

    # Socket to receive order updates
    update_socket = context.socket(zmq.PULL)
    # update_socket.bind("tcp://*:5556")
    update_socket.bind("tcp://*:5558")

    def listen_for_updates():
        while True:
            message = update_socket.recv_string()
            print(f"Received update: {message}")

    # Start listening for updates
    listen_for_updates()

def zmq_send_order_updates(context):
    # Socket to send orders
    order_socket = context.socket(zmq.PUSH)
    # order_socket.connect("tcp://localhost:5555")
    order_socket.connect("tcp://localhost:5557")
    def send_order():
        order_socket.send_string("Order Data Here")
        print("Sent Order")
    # Simulate sending an order
    send_order()
    send_order()
    send_order()
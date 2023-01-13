import socket
import pickle


class Server:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def accept_connections(self):
        while True:
            client, address = self.server.accept()
            print(f"Connection from {str(address)} has been established.")
            data = {'name': 'Youssef', 'age': 21}
            data = pickle.dumps(data)
            client.send(data)
            client.close()


server = Server()
server.accept_connections()

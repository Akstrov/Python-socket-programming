import socket
import pickle


class Client:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send_data(self, data):
        self.client.sendall(bytes(data, "utf-8"))

    def receive_data(self):
        data = self.client.recv(4096)
        data = pickle.loads(data)
        return data

    def close_connection(self):
        self.client.close()


client = Client()
# client.send_data("Hello, Server!")
print(client.receive_data())
client.close_connection()

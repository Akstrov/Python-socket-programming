# It creates a socket object, connects to the server, sends data to the server, receives data from the
# server, and closes the connection to the server
import socket
import pickle


class Client:
    def __init__(self, host='127.0.0.1', port=5000):
        """
        The function __init__() is a constructor that is called when an object of a class is
        instantiated
        
        :param host: The IP address of the server, defaults to 127.0.0.1 (optional)
        :param port: The port number that the server is listening on, defaults to 5000 (optional)
        """
        self.host = host
        self.port = port
        # Creating a socket object and connecting to the server.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send_data(self, data):
        """
        It takes a string, converts it to bytes, and sends it to the server
        
        :param data: The data to send to the server
        """
        self.client.sendall(bytes(data, "utf-8"))

    def receive_data(self):
        """
        It receives data from the server and unpickles it
        :return: The data is being returned.
        """
        data = self.client.recv(4096)
        data = pickle.loads(data)
        return data

    def close_connection(self):
        """
        It closes the connection to the server
        """
        self.client.close()


client = Client()
# client.send_data("Hello, Server!")
print(client.receive_data())
client.close_connection()

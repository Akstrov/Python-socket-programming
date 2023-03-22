# It creates a server that accepts connections and sends a dictionary to the client
import socket
import pickle


class Server:
    def __init__(self, host='127.0.0.1', port=5000):
        """
        The function takes in two arguments, host and port, and sets them to the variables self.host and
        self.port. Then, it creates a socket object and binds it to the host and port. Finally, it
        listens for incoming connections

        :param host: The IP address of the server, defaults to 127.0.0.1 (optional)
        :param port: The port number that the server will listen on, defaults to 5000 (optional)
        """
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def accept_connections(self):
        """
        It accepts a connection from a client, prints a message, sends a pickled dictionary to the
        client, and closes the connection
        """
        while True:
            client, address = self.server.accept()
            print(f"Connection from {str(address)} has been established.")
            data = {'name': 'Youssef', 'age': 21}
            data = pickle.dumps(data)
            client.send(data)
            client.close()


server = Server()
server.accept_connections()

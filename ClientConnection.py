import socket
import pickle


class ClientConnection:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.37"
        self.port = 13010
        self.addr = (self.server, self.port)

    # connects the players to the server
    def connect(self):
        self.client.connect(self.addr)
        self.client.send(pickle.dumps("getPos"))
        return self.getPos()

    # gets the position of the objects
    def getPos(self):
        return pickle.loads(self.client.recv(2048))

    # gives the position of the new platform to the server
    def sendPlat(self, platY):
        self.client.send(pickle.dumps((platY, "sendPlat")))

    # gets the position of the new platform from the server
    def getPlat(self):
        self.client.send(pickle.dumps("newPlat"))
        return pickle.loads(self.client.recv(2048))

    # gets the number of players connected to the server
    def getPlayerCount(self):
        self.client.send(pickle.dumps("getPlayerCount"))
        return pickle.loads(self.client.recv(2048))

    def dead(self):
        self.client.send(pickle.dumps("Dead"))

    # sends data to the server and receives data other client data
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


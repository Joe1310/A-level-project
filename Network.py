import pygame
import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.37"
        self.port = 13010
        self.addr = (self.server, self.port)
        self.p = self.connect()

# gets the position of the objects
    def getP(self):
        return self.p

# connects the players to the server
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

# sends data from the server to the client and back to the server
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


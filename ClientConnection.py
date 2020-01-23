import pygame
import socket
import pickle


class ClientConnection:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.16.8.47"
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

    # sends data to the server and receives data other client data
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

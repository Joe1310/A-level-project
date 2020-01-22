import pygame
import socket
import pickle


class ClientConnection:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.16"
        self.port = 13009
        self.addr = (self.server, self.port)

    # connects the players to the server
    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.send(pickle.dumps("getPos"))
            self.pos = self.getPos()
            return self.pos
        except:
            print("NIGGER THIS NO WORKING")
            pass

        # gets the position of the objects

    def getPos(self):
        return pickle.loads(self.client.recv(2048))

    # sends data to the server and recieves data other client data
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

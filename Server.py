import socket
from _thread import *
import pickle

# Local Ip (IPV4 FROM CMD IPCONFIG, DEVICE SPECIFIC)
server = socket.gethostbyname(socket.gethostname())

# Server Port
port = 13010

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The try and except are used to test to see if the port is open. If it is open it will bind the server to the port and
# if not then the program will print out e to show that the port is in use (e for error).
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# opens up port to allow us to begin to use it to connect multiple clients together. Inside the brackets limits the
# number of possible connections
s.listen(2)
print("Waiting for connection, Server Initiated")

playerPositions = [[100, 100], [400, 100]]


# client = connection, addr = address
def threaded_client(client, player):
    while True:
        data = pickle.loads(client.recv(2048))
        # checks to see if any data is being received from the client, if not it assumes that the client is
        # disconnected and stops running in the background
        if data:
            if data == "getPos":
                reply = (playerPositions[player])
            # reply with other player position
            else:
                if player == 0:
                    playerPositions[0] = data
                    reply = playerPositions[1]
                else:
                    playerPositions[1] = data
                    reply = playerPositions[0]
        else:
            print("Lost Connection")
            client.close()
            break

        # sends data back to clients
        client.sendall(pickle.dumps(reply))


# keeps track of current playerPositions data
currentPlayer = 0
while True:
    connection, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (connection, currentPlayer))
    currentPlayer += 1

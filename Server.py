import socket
from _thread import *
from Player import *
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

playerPositions = [[0,0],[0,0]]

# conn = connection, addr = address
def threaded_client(conn, player):
    conn.send(pickle.dumps(playerPositions[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            playerPositions[player] = data
            print(playerPositions)

            # checks to see if any data is being received from the client, if not it assumes that the client is
            # disconnected and stops running in the background
            if not data:
                print("Disconnected")
                break

            else:
                if player == 1:
                    reply = playerPositions[0]

                else:
                    reply = playerPositions[1]
                print("Received:", data)
                print("Sending:", reply)

            # sends data back to clients
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost Connection")
    conn.close()
    return

# keeps track of current playerPositions data
CurrentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,CurrentPlayer))
    CurrentPlayer += 1
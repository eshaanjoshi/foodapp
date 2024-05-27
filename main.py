import socket

s = socket.socket()

print("Socket successfully created")

port = 40674

s.bind(('', port))

print(f"socket binded to {port}")

s.listen(5)

print("socket is listening")

while True:
    c, addr = s.accept()
    print ('Got connection from', addr)
    c.send(b'Thank you for connecting')
    c.close()
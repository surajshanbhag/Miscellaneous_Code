import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:

    message='OK'
    amount_received = 0
    amount_expected = len(message)

    while True:
# Send data
        message = 'OK'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

# Look for the response
        data = sock.recv(16)
        amount_received = len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()


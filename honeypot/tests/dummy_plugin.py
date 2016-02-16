import socket
import sys
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 23)
print  'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

class server(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address


    while True:
        # Wait for a connection
        print  'waiting for a connection'
        connection, client_address = sock.accept()
        try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
           # while True:
            #    data = connection.recv(16)
             #   print 'received "%s"' % data
             #   if data:
              #      print , 'sending data back to the client'
               #     connection.sendall(data)
               # else:
                #    print 'no more data from', client_address
                #    break

        finally:
            # Clean up the connection
            connection.close()
            break


if __name__ == "__main__":
    pass
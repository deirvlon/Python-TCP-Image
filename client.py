import numpy as np
import cv2
import socket


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 7777)
print( 'connecting to %s port %s' % server_address)
sock.connect(server_address)
for i in range(1,80):
    try:
    
        # Get Camera frames
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            _, frame = cap.read()
            #send data
            sock.sendall(bytes(cv2.resize(frame, (480,270)))) #resize frame, then convert it in to bytes
        
        cap.release()
        cv2.destroyAllWindows()
        
        if (cv2.waitKey(1) and 0xFF == ord('q')):
                    break

        # # Look for the response
        # amount_received = 0
        # amount_expected = len(message)
        
        # while amount_received < amount_expected:
        #     data = sock.recv(388800)
        #     amount_received += len(data)
        #     print(sys.stderr, 'received "%s"' % data)

    finally:
        print("END")

print('closing socket')
sock.close()

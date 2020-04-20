import numpy as np
import cv2
import socket


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 7777) 
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)


def applyImage(data):
	decoded = np.frombuffer(data, dtype=np.uint8)
	decoded = decoded.reshape((270, 480,3))
	return decoded;


while True:
    # Wait for a connection
    print( 'waiting for a connection')
    connection, client_address = sock.accept()


    try:
        print( 'connection from', client_address)

        # Receive the data in once
        while True:
            #Image size is (480x270), with 3 color channel : (480 x 270) x 3 = 388800 bytes
            data = connection.recv(388800) 

            if data:
                #Visualize the received data
            	cv2.imshow('IMG',applyImage(data))
            	if (cv2.waitKey(1) and 0xFF == ord('q')):
                    break

            else:
                print('no more data from', client_address);
                break;
                
               


    finally:
        # Clean up the connection
        connection.close()
        cv2.waitKey(0)
        cv2.destroyAllWindows()


connection.close()

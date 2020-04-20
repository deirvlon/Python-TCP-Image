# Python-TCP-Image
Send and Receive Image over TCP connection

# Client:
Get camera frame as numpy array,
Convert it into bytes to be able to send over net

# Server:
Receives bytes (data = connection.recv(388800))
Convert bytes into numpy array
After converting we get 1 dimentional array shape of (388800,1)
Then we reshape this array into (270, 480, 3)
This is the form of cv2 image 


# Convert:
Numpy to bytes 
bytes to Numpy
Link: https://stackoverflow.com/questions/49511753/python-byte-image-to-numpy-array-using-opencv/61273896#61273896



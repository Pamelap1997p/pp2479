# import socket module
from socket import *
import  sys  # In order to terminate the program


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(('', port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...') need to comment out gradescope doesn’t like print statements
        connectionSocket, addr = serverSocket.accept()

        # Fill in start      #Fill in end
        try:
            message = connectionSocket.recv(1024)  # need to enter the maximum size of data received at once for the parameter 1024
            # print message,'::',message.split()[0],':',message.split()[1] -not sure what this is but you don’t need it
            # Fill in start    #Fill in end
            filename = message.split()[1]
            # print filename,'||',[1:] No print statement
            f = open(filename[1:])
            outputdata = f.read()

            # Fill in start
            # print outputdata
            # Fill in end

            # Send one HTTP header line into socket
            # Fill in start
            # Need to send a http header
            connectionSocket.send('HTTP/1.0 200 OK\r\n\n\n'.encode())
        # connectionSocket.send(outputdata) #notsure if this is needed.  You need to write out the header see above.

        # Fill in end

        # Send the content of the requested file to the client

            for i in range(0, len(outputdata)):

             connectionSocket.send(outputdata[i].encode())  # needs to be encoded see above for how to encode


             connectionSocket.send("\r\n".encode())#this is needed dont comment out

             connectionSocket.close()

         except IOError:

# Send response message for file not found (404)
# Fill in start

# print '404 Not Found'
             connectionSocket.send('HTTP/1.1 404 Not Found\n\n\r\n'.encode())  # need the encode statement here

# Fill in end

# Close client socket
# Fill in start

            connectionSocket.close()
# Fill in end


            serverSocket.close()
            sys.exit()  # Terminate the program after sending the corresponding data

            if __name__ == "__main__":
             webServer(13331)
           

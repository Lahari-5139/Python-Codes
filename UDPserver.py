from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    numbers,clientAddress = serverSocket.recvfrom(2048)
    print "data received is " ,numbers
    temp = map(lambda x:int(x),numbers.split())
    temp.sort()
    temp.reverse()
    print "Sorted data in decreasing order is ",str(temp)
    sorted_numbers = str(temp)
    serverSocket.sendto(sorted_numbers, clientAddress)

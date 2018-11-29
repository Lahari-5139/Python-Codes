from socket import *
serverName = '172.16.86.173'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
numbers = raw_input("enter the numbers:")
clientSocket.send(numbers)
modifiednumbers = clientSocket.recv(1024)
print 'From Server:', modifiednumbers
clientSocket.close()
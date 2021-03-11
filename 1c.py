import socket

 

msgFromClient       = "Oi servidor! Envie dados de disco total e de disco disponivel..."

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 9991)

bufferSize          = 1024

 

# criando um socket udp ao lado do cliente

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# enviando socket criado

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
 

msg = "Messagem do servidor: {}".format(msgFromServer[0])

print(msg)

import socket, psutil


serverAddressPort   = ("127.0.0.1", 9991)
bufferSize          = 1024


def client_udp():
    msgFromClient       = "Oi servidor! Envie dados de disco total e de disco disponivel..."
    bytesToSend         = msgFromClient.encode("utf-8")

    # criando um socket udp ao lado do cliente
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # enviando socket criado

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Messagem do servidor: {}".format(msgFromServer[0])
    print(msg)
    
    


if __name__ == '__main__':
    client_udp()

 

print('Servidor UDP escutando...')
print('Esperando receber na porta', localPort, '...')

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Messagem do cliente:{}".format(message)
    clientIP  = "IP do cliente:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
   

    # enviando resultado ao cliente

    UDPServerSocket.sendto(bytesToSend, address)

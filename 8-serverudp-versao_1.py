import socket, psutil

 
d =  psutil.disk_usage('.')
dt = round(d.total/(1024**3))
df = round(d.free/(1024**3))

def server_udp():

    msgFromServer = 'Disco total {} GB - Disco disponivel {} GB'.format(dt, df) 
    bytesToSend = str.encode(msgFromServer) 

    # Criando socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) 

    # Bind 

    UDPServerSocket.bind((localIP, localPort)) 
    print('Servidor UDP escutando...')
    print('Esperando receber na porta', localPort, '...')

    # ouvido datagrams indefinidos
    while True:

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Messagem do cliente:{}".format(message)
        clientIP  = "IP do cliente:{}".format(address)
        
        print(clientMsg)
        print(clientIP)
       

        # enviando resultado ao cliente
        UDPServerSocket.sendto(bytesToSend, address)


if __name__ == '__main__':
    server_udp()


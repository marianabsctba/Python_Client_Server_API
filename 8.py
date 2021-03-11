import socket, psutil

 

localIP     = "127.0.0.1"

localPort   = 9991

bufferSize  = 1024

 
d =  psutil.disk_usage('.')

dt = round(d.total/(1024**3))

df = round(d.free/(1024**3))

msgFromServer = 'Disco total {} GB - Disco disponivel {} GB'.format(dt, df) 

bytesToSend = str.encode(msgFromServer)

 

# Criando socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind 

UDPServerSocket.bind((localIP, localPort))

 

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

#CLIENTE UDP

import socket

clientUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (socket.gethostname(), 9991)


def clientu():
    try:
        print('Esperando o servidor na porta', 9991)
        ask = input("Quer receber dados de disco? (y/n):")
        
        clientUdp.sendto(ask.encode(), server)
        (msg, cliente) = clientUdp.recvfrom(1024)
        print(msg.decode('utf-8'))
        clientUdp.close()

    except Exception as error:
        print(error)


if __name__ == '__main__':
    clientu()

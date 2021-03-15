#SERVER UDP

import socket
import psutil

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind((socket.gethostname(), 9991))

disco = psutil.disk_usage('.')
total = round(disco.total / (1024 **3), 2)
disponivel = round(disco.free / (1024**3), 2)
utilizado = round(disco.used / (1024**3), 2)


def serveru():
    print("Esperando cliente na porta", 9991)
    while True: # espera indefinidamente
        try:
            (msg, client) = udpServer.recvfrom(1024)
            if msg.decode() == 'y':
                udpServer.sendto('\ntotal : {}GB\nlivre :{}GB\nutilizado: {}GB'.format(total, disponivel, utilizado).encode('utf-8'), client)

            else:
                udpServer.sendto('Erro: Digite (s).'.encode('utf-8'), client)

            udpServer.close()

        except Exception as error:
            print(error)


if __name__ == '__main__':
    serveru()

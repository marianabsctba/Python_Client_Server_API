import socket, os


def server_program():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8881

    socket_server.bind((host, port))
    socket_server.listen()

    print("Servidor de nome", host, "esperando conexão na porta", port)

    while True:
        (socket_client,addr) = socket_server.accept() # espera indefinidamente
        print("Conectado a:", str(addr))

        msg = socket_client.recv(2048)
        name = msg.decode('ascii')

        if os.path.isfile(name):
            l = os.stat(name).st_size
            socket_client.send(str(l).encode('ascii'))

            fil = open(name, 'rb')
            bytes = fil.read(4096)

            while bytes:
                socket_client.send(bytes)
                bytes = fil.read(4096)

            fil.close()
        else:
            print("Arquivo não encontrado...")
            socket_client.send('-1'.encode('ascii'))
            socket_client.close()

    socket_servidor.close()

if __name__ == '__main__':
    server_program()

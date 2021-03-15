import socket, sys, os, time

name = input('Qual o nome do arquivo com extensao? ')


def print_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    text = 'Fazendo o download... '
    text = text + '{:<.2f}'.format(kbytes) + ' KB '
    text = text + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(text)

	
def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	    s.connect((socket.gethostname(), 8881))
	    s.send(name.encode('ascii'))
	    msg = s.recv(12)
	    lenght = int(msg.decode('ascii'))
	    if lenght >= 0:
		print('Arquivo encontrado... aguarde...')
		time.sleep(3)
		fil = open('download\\'+name, "wb")
		summ = 0
		bytes = s.recv(4096)

		while bytes:
		    fil.write(bytes)
		    summ = summ + len(bytes)
		    os.system('cls')
		    print_status(summ, lenght)
		    bytes = s.recv(4096)
		fil.close()


	except Exception as erro:
		print(str(erro))

	s.close()

if __name__ == '__main__':
    main()

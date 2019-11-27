import socket, select, string, sys

# apresentacao cliente
def prompt() :
	sys.stdout.write('<You> ')
	sys.stdout.flush()

#main function
if __name__ == "__main__":
	
	if(len(sys.argv) < 3) :
		print 'Usage : python cliente.py <ip server> port'
		sys.exit()
	
	host = sys.argv[1]
	port = int(sys.argv[2])
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	
	# conectando no servidor remoto
	try :
		s.connect((host, port))
	except :
		print 'Unable to connect'
		sys.exit()
	
	print 'Conectando no servidor de chat...'
	prompt()
	
	while 1:
		socket_list = [sys.stdin, s]
		
		# capturar sockets que estao prontos para transmissao
		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
		
		for sock in read_sockets:
			# quando recebe mensagem do servidor
			if sock == s:
				data = sock.recv(4096)
				if not data :
					print '\nDisconectado do servidor de chat'
					sys.exit()
				else :
					#print data
					sys.stdout.write(data)
					prompt()
			
			# quando user digita uma mensagem
			else :
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()
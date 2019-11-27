from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Send:
    def __init__(self):
        self.__msg = ''
        self.new = True
        self.con = None
    
    def put(self, msg):
        self.__msg = msg
        if self.con != None:
            self.con.send(str.encode(self.__msg))
    
    def get(self):
        return self.__msg
    
    def loop(self):
        return self.new

def esperar(tcp, send, host = 'localhost', port = 5000):
    destino = (host, port)
    tcp.connect(destino)

    while send.loop():
        print('Conectado a ', host, '.')
        send.con = tcp

        while send.loop():
            msg = tcp.recv(1024)
            if not msg: break
            print(str(msg, 'utf-8'))

if __name__ == '__main__':
    print('Digite o nome ou IP do servidor (localhost): ')
    host = input()

    if host == '':
        host = '127.0.0.1'
    
    tcp = socket(AF_INET, SOCK_STREAM)
    send = Send()
    
    processo = Thread(target=esperar, args=(tcp, send, host))
    processo.start()
    print('')

    msg = input()
    while True:
        send.put(msg)
        msg = input()

    processo.join()
    tcp.close()
    exit()

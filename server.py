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

def esperar(tcp, send, host = '', port = 5000):
    origem = (host, port)
    tcp.bind(origem)
    tcp.listen(1)

    while True:
        con, cliente = tcp.accept()
        print('Cliente', cliente, ' conectado!')
        send.con = con

        while True:
            msg = con.recv(1024)
            if not msg: break
            print(str(msg, 'utf-8'))

if __name__ == '__main__':
    tcp = socket(AF_INET, SOCK_STREAM)
    send = Send()
    processo = Thread(target = esperar, args = (tcp, send))
    processo.start()

    print('Iniciando o servidor de chat!')
    print('Aguarde alguém conectar!')

    msg = input()
    while True:
        send.put(msg)
        msg = input()
    
    processo.join()
    tcp.close()
    exit()
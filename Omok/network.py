from pyclbr import Function
import socket
import pickle

hostname = socket.gethostname()

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(hostname) #ipv4 주소
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode('utf-8'))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)




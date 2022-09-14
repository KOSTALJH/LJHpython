import os
import socket
import json
import threading
import time
import sys
from chess import chessboard
t=chessboard()
id=1#   id
def handle():
    while (not t.is_end()):
        for c in socks:
            global id
            json_string0 = json.dumps(t._chessboard__board)
            c.sendto(json_string0.encode('utf-8'), address)
            msg1 = 'Your id is %d,input your next drop' % id + "\r"
            c.send(msg1.encode('utf-8'))
            msg2x = c.recv(1024)
            msg2y = c.recv(1024)
            x = int(msg2x.decode('utf-8'))
            y = int(msg2y.decode('utf-8'))
            print('processing......')
            if t.drop_chess(x, y, id):
                json_string = json.dumps(t._chessboard__board)
                c.sendto(json_string.encode('utf-8'), address)
            else:
                msg3 = '_________Illegal Input,Please Check Again_________'
                c.send(msg3.encode('utf-8'))
                continue
            id = changeid(id)
def clear():
    os.system('cls')
def changeid(id):
    if id==1:
        return 2
    elif id==2:
        return 1
    else:
        return 0
#    socket   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        
host = socket.gethostname()
port = 9999
#      
s.bind((host, port))
address=(host, port)
#        ，     
s.listen(2)
socks=[]
th = threading.Thread(target=handle)
th.start()
while 1:
    c, addr = s.accept()
    print('connected from:', addr)
    socks.append(c)
s.close()
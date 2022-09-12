from locale import currency
import socket
from _thread import *
import pickle

hostname = socket.gethostname()
server = socket.gethostbyname(hostname) #ipv4 주소 적을것
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


currentId = "0"
pos = [0,1]
s.listen(2)
print("연결 대기 중 ...")


def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(4096)
            reply = data.decode('utf-8')
            
            if not data :
                print("P : 연결이 끊겼습니다.")
                break
            else:
                print("P : 착신 : ", reply)
                print("P : 송신 : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
        

    print("연결이 끊겼습니다.")
    conn.close()

while True:
    conn, addr = s.accept()
    print("연결 : ",addr)



    start_new_thread(threaded_client, (conn,))
    



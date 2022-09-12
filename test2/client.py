import socket
import time
import pygame

bg_color = (255, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

window_width = 900
window_height = 700
board_width = 500
grid_size = 30

#    socket   
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        
#host = socket.gethostname()
host='192.168.45.145'
#      
port = 9999
#     ，       
c.connect((host, port))
address=(host, port)
def main():
    pygame.init()
    surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Omok game")
    surface.fill(bg_color)

    while 1:
 #s=c.accept()
        print('')
        print('__________________wait__________________')
        msg0 = c.recv(2048).decode('utf-8') #     1024
        for x in msg0:
            if x == '[':
                print('')
            else:
                print(x, end='')
        print('')
        msg1 = c.recv(1024)#      
        print (msg1.decode('utf-8'))
        time.sleep(1)
        x = input('x=')
        y = input('y=')
        c.send(x.encode('utf-8'))
        c.send(y.encode('utf-8'))
        msg3 = c.recv(2048).decode('utf-8')#    1024
        if msg3=='_________Illegal Input,Please Check Again_________':
            print(msg3)
            continue
        else:
  #print(msg3)
            for x in msg3:
                if x=='[':
                    print('')
                else:
                    print(x, end='')
            print('')
            print('__________________wait__________________')
        print('')
    c.close()

if __name__ == '__main__':
    main()
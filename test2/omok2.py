from chess import chessboard
def changeid(id):
    if id==1:
        return 2
    elif id==2:
        return 1
    else:
        return 0
t=chessboard()
id=1#   id
t.draw()
while (not t.is_end()):#end  
    print('your id is %d,input your next drop(x,y)'% id)
    x=input()
    y=input()
    x=int(x)
    y=int(y)
    if t.drop_chess(x,y,id):
        t.draw()
    else:
        print('_________Illegal Input,Please Check Again_________')
        continue
    id=changeid(id)
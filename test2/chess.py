import os
class chessboard(object):
    def __init__(self):
        self.size = 16
  #     
        self.__board=[[' ' for n in range(self.size)] for m in range(self.size)]
        n = 0
  #      
        while n < self.size:
            ntr=str(n)
            self.__board[0][n] = ntr.zfill(2)
            self.__board[n][0] = ntr.zfill(2)
            n=n+1
        self.id=0
 #    
    def is_end(self):
        ch_stack=[]
  #   
        for i in range(self.size):
            for j in range(self.size):
    #      
                chess=self.__board[i][j]
                if len(ch_stack)==5 and ch_stack[-1]=='* ':
                    print('winner=id 1')
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == '@ ':
                    print('winner=id 2')
                    return 2

                if chess==' ':
                    ch_stack.clear()
                else:
                    if (not ch_stack) or ch_stack[-1] == chess:
                        ch_stack.append(chess)
                    else:
                        ch_stack.clear()
                        ch_stack.append(chess)
            ch_stack.clear()
        ch_stack.clear()
  #   
        for j in range(self.size):
            for i in range(self.size):
    #      
                if len(ch_stack)==5 and ch_stack[-1]=='* ':
                    print('winner=id 1')
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == '@ ':
                    print('winner=id 2')
                    return 2
                chess=self.__board[i][j]
                if chess==' ':
                    ch_stack.clear()
                else:
                    if (not ch_stack) or ch_stack[-1] == chess:
                        ch_stack.append(chess)
                    else:
                        ch_stack.clear()
                        ch_stack.append(chess)
            ch_stack.clear()
        ch_stack.clear()
  #    
  #   
        for i in range(self.size):
            for j in range(1,self.size):
    #      
                if len(ch_stack)==5 and ch_stack[-1]=='* ':
                    print('winner=id 1')
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == '@ ':
                    print('winner=id 2')
                    return 2

                if i+j<self.size:
                    chess=self.__board[i+j][j]
                    if chess==' ':
                        ch_stack.clear()
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
  #   
        for i in range(self.size):
            for j in range(1,self.size):
    #      
                if len(ch_stack)==5 and ch_stack[-1]=='* ':
                    print('winner=id 1')
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == '@ ':
                    print('winner=id 2')
                    return 2
                if i+j<self.size:
                    chess=self.__board[j][j+i]
                    if chess==' ':
                        ch_stack.clear()
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
  #    
  #   
        for i in range(self.size):
            for j in range(1,self.size):
    #      
                if len(ch_stack)==5 and ch_stack[-1]=='* ':
                    print('winner=id 1')
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == '@ ':
                    print('winner=id 2')
                    return 2
                if self.size-i-j+1>0:
                    chess=self.__board[self.size-i-j][j]
                    if chess==' ':
                        ch_stack.clear()
                    elif not chess:
                        break
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
  #   
        for i in range(self.size):
            for j in range(1,self.size):
    #       
                if len(ch_stack) == 5 and ch_stack[-1] == '* ':
                    print('winner=id 1')
                    return 1
                elif len(ch_stack) == 5 and ch_stack[-1] == '@ ':
                    print('winner=id 2')
                    return 2
                if self.size-i-j> 0:
                    chess = self.__board[j][self.size-i-j]
                    if chess == ' ':
                        ch_stack.clear()
                    elif not chess:
                        break
                    else:
                        if (not ch_stack) or ch_stack[-1] == chess:
                            ch_stack.append(chess)
                        else:
                            ch_stack.clear()
                            ch_stack.append(chess)
                else:
                    break
            ch_stack.clear()
        ch_stack.clear()
        return 0
        
    def draw(self):
  #clear()
        for x in self.__board:
            print(x)
            return 0


    def drop_chess(self,x,y,id):
        if id==1 and self.__board[x][y]==' ':
            self.__board[x][y]='* '
            return 1
        elif id==2 and self.__board[x][y]==' ':
            self.__board[x][y]='@ '
            return 1
        else:
            return 0
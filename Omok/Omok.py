import pygame, sys
from pygame.locals import *
from rule import *
import socket
from network import Network

bg_color = (128, 128, 128)
black = (0, 0, 0)
blue = (0, 50, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)

window_width = 800
window_height = 500
board_width = 500
grid_size = 30

fps = 60
fps_clock = pygame.time.Clock()


hostname = socket.gethostname()
server = socket.gethostbyname(hostname) #ipv4 주소 적을것
port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.connect((server, port))



def main():
    pygame.init()
    surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Omok game")
    surface.fill(bg_color)
    omok = Omok(surface)
    menu = Menu(surface)
    while True:
        run_game(surface, omok, menu)
        menu.is_continue(omok)
        

    
def run_game(surface, omok, menu):
    omok.init_game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                menu.terminate()
            elif event.type == MOUSEBUTTONUP:
                if not omok.check_board(event.pos):
                    if menu.check_rect(event.pos, omok):
                        omok.init_game()

        

        if omok.is_gameover:
            return

        pygame.display.update()
        fps_clock.tick(fps)

class Omok(object):
    def __init__(self, surface):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.menu = Menu(surface)
        self.rule = Rule(self.board)
        self.surface = surface 
        self.pixel_coords = []
        self.set_coords()
        self.set_image_font()
        self.is_show = True
        self.net = Network()
        self.net.id
        
    #매 게임마다 초기화 필요한 함수
    def init_game(self):
        self.turn  = black_stone
        self.draw_board()
        self.menu.show_msg(empty)
        self.init_board()
        self.coords = []
        self.redos = []
        self.id = 1
        self.is_gameover = False
        self.is_forbidden = False

    #이미지 폰트
    def set_image_font(self):
        black_img = pygame.image.load('C:/Users/User/project/doit/Omok/image/black.png')
        white_img = pygame.image.load('C:/Users/User/project/doit/Omok/image/white.png')
        self.last_w_img = pygame.image.load('C:/Users/User/project/doit/Omok/image/white_a.png')
        self.last_b_img = pygame.image.load('C:/Users/User/project/doit/Omok/image/black_a.png')
        self.board_img = pygame.image.load('C:/Users/User/project/doit/Omok/image/board.png')
        self.forbidden_img = pygame.image.load('C:/Users/User/project/doit/Omok/image/forbidden.png')
        self.font = pygame.font.Font("freesansbold.ttf", 14)
        self.black_img = pygame.transform.scale(black_img, (grid_size, grid_size))
        self.white_img = pygame.transform.scale(white_img, (grid_size, grid_size))

    #보드 초기화
    def init_board(self):
        for y in range(board_size):
            for x in range(board_size):
                self.board[y][x] = 0

    #보드 그리기
    def draw_board(self):
        self.surface.blit(self.board_img, (0, 0))

    #바둑돌 그리는 함수
    def draw_image(self, img_index, x, y):
        img = [self.black_img, self.white_img, self.last_b_img, self.last_w_img, self.forbidden_img]
        self.surface.blit(img[img_index], (x, y))

    #바둑알에 번호 보여주는 함수
    def show_number(self, x, y, stone, number):
        colors = [white, black, red, red]
        color = colors[stone]
        self.menu.make_text(self.font, str(number), color, None, y + 15, x + 15, 1)

    #바둑알 번호 지워주는 함수
    def hide_numbers(self):
        for i in range(len(self.coords)):
            x, y = self.coords[i]
            self.draw_image(i % 2, x, y)
        if self.coords:
            x, y = self.coords[-1]
            self.draw_image(i % 2 + 2, x, y)

    #바둑알 번호 써주는 함수
    def show_numbers(self):
        for i in range(len(self.coords)):
            x, y = self.coords[i]
            self.show_number(x, y, i % 2, i + 1)
        if self.coords:
            x, y = self.coords[-1]
            self.draw_image(i % 2, x, y)
            self.show_number(x, y, i % 2 + 2, i + 1)

    #금수 체크 함수
    def check_forbidden(self):
        if self.turn == self.turn_change():
            coords = self.rule.get_forbidden_points(self.turn)
            while coords:
                x, y = coords.pop()
                x, y = x * grid_size + 25, y * grid_size + 25
                self.draw_image(4, x, y)
            self.is_forbidden = True

    #돌 그리는 함수
    def draw_stone(self, coord, stone, increase):
        if self.is_forbidden:
            self.draw_board()
        x, y = self.get_point(coord)
        self.board[y][x] = stone
        self.hide_numbers()
        if self.is_show:
            self.show_numbers()
        self.id += increase
        self.turn_change()
        self.check_forbidden()

        



        
    #픽셀 좌표 구하는 함수
    def set_coords(self):
        for y in range(board_size):
            for x in range(board_size):
                self.pixel_coords.append((x * grid_size + 25, y * grid_size + 25))

    #마우스 포인트 좌표 찾는 함수
    def get_coord(self, pos):
        for coord in self.pixel_coords:
            x, y = coord
            rect = pygame.Rect(x, y, grid_size, grid_size)
            if rect.collidepoint(pos):
                return coord
        return None

    #픽셀 좌표를 board list에 사용될 순서로 바꿔주는 함수
    def get_point(self, coord):
        x, y = coord
        x = (x - 25) // grid_size
        y = (y - 25) // grid_size
        return x, y

    #마우스 클릭했을 때 호출, 게임판 밖이면 False리턴, 좌표가 반환됬으면 공백 체크
    #공백이 아닌 곳이면 True리턴하고 끝, 공백인 곳이 클릭됬으면 
    #좌표 저장하고 보드에 그린다음 게임 끝났는지 확인. 게임 끝났으면 표시함.                     
    def check_board(self, pos):
        coord = self.get_coord(pos)
        if not coord:
            return False
        
        x, y = self.get_point(coord)
        
        board = self.board[y][x]
        self.net.send(str.encode(str(board)))
        
        data = s.recv(4096).decode()
        self.board[y][x] = data
        
        

        if self.board[y][x] != empty:
            print("occupied")
            return True

        if self.turn == black_stone:
            if self.rule.forbidden_point(x, y, self.turn):
                print("forbidden point")
                return True

        self.coords.append(coord)
        self.draw_stone(coord, self.turn, 1)
        if self.check_gameover(coord, self.turn_change()):
            self.is_gameover = True
            s.close()
        if len(self.redos):
            self.redos = []

        return True

    #5개 이상 붙이거나 보드가 꽉 찬 경우 게임 종료 시키는 함수
    def check_gameover(self, coord, stone):
        x, y = self.get_point(coord)
        if self.id > board_size * board_size:
            self.show_winner_msg(stone)
            return True
        elif self.rule.is_gameover(x, y, stone):
            self.show_winner_msg(stone)
            return True
        return False

    #턴 바꾸는 함수이나 실패...
    def turn_change(self):
        player = str(self.net.id)
        turn = 1
        if player ==  0:
            turn = black_stone

        elif player == 1:
            turn = white_stone
        
        return turn

    #게임 끝났을 때 메세지 띄워주는 함수
    def show_winner_msg(self, stone):
        for i in range(3):
            self.menu.show_msg(stone)
            pygame.display.update()
            pygame.time.delay(200)
            self.menu.show_msg(empty)
            pygame.display.update()
            pygame.time.delay(200)
        self.menu.show_msg(stone)

        
class Menu(object):
    def __init__(self, surface):
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.surface = surface
        self.draw_menu()

    #메뉴 그려주는 함수
    def draw_menu(self):
        top, left = window_height - 30, window_width - 200
        self.new_rect = self.make_text(self.font, 'New Game', blue, None, top - 30, left)
        self.quit_rect = self.make_text(self.font, 'Quit Game', blue, None, top, left)
        self.show_rect = self.make_text(self.font, 'Hide Number  ', blue, None, top - 60, left)
       
    #종료할 때 메세지 띄워주는 함수
    def show_msg(self, msg_id):
        msg = {
            empty : '                                    ',
            black_stone: 'Black win!!!',
            white_stone: 'White win!!!',
            tie: 'Tie',
        }
        center_x = window_width - (window_width - board_width) // 2
        self.make_text(self.font, msg[msg_id], black, bg_color, 30, center_x, 1)

    #글자 적는 함수
    def make_text(self, font, text, color, bgcolor, top, left, position = 0):
        surf = font.render(text, False, color, bgcolor)
        rect = surf.get_rect()
        if position:
            rect.center = (left, top)
        else:    
            rect.topleft = (left, top)
        self.surface.blit(surf, rect)
        return rect

    #바둑돌 번호 숨기는 함수
    def show_hide(self, omok):
        top, left = window_height - 90, window_width - 200
        if omok.is_show:
            self.make_text(self.font, 'Show Number', blue, bg_color, top, left)
            omok.hide_numbers()
            omok.is_show = False
        else:
            self.make_text(self.font, 'Hide Number  ', blue, bg_color, top, left)
            omok.show_numbers()
            omok.is_show = True

    
    def check_rect(self, pos, omok):
        if self.new_rect.collidepoint(pos):
            return True
        elif self.show_rect.collidepoint(pos):
            self.show_hide(omok)
        elif self.quit_rect.collidepoint(pos):
            self.terminate()
        return False
    
    #끝내는 함수
    def terminate(self):
        pygame.quit()
        sys.exit()

    #재시작 함수
    def is_continue(self, omok):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEBUTTONUP:
                    if (self.check_rect(event.pos, omok)):
                        return
            pygame.display.update()
            fps_clock.tick(fps)    

    
if __name__ == '__main__':
    main()

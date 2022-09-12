board_size = 15
empty = 0
black_stone = 1
white_stone = 2
last_b_stone = 3
last_a_stont = 4
tie = 100

class Rule(object):
    def __init__(self, board):
        self.board = board

    #유효 영역 체크
    def is_invalid(self, x, y):
        return (x < 0 or x >= board_size or y < 0 or y >= board_size)
    
    #돌 놓거나 들어내는 함수
    def set_stone(self, x, y, stone):
        self.board[y][x] = stone

    #같은 돌 찾기
    def get_xy(self, direction):
        list_dx = [-1, 1, -1, 1, 0, 0, 1, -1]
        list_dy = [0, 0, -1, 1, -1, 1, -1, 1]
        return list_dx[direction], list_dy[direction]

    #돌 카운트
    def get_stone_count(self, x, y, stone, direction):
        x1, y1 = x, y
        cnt = 1
        for i in range(2):
            dx, dy = self.get_xy(direction * 2 + i)
            x, y = x1, y1
            while True:
                x, y = x + dx, y + dy
                if self.is_invalid(x, y) or self.board[y][x] != stone:
                    break;
                else:
                    cnt += 1
        return cnt
    
    #게임 종료 확인
    def is_gameover(self, x, y, stone):
        for i in range(4):
            cnt = self.get_stone_count(x, y, stone, i)
            if cnt >= 5:
                return True
        return False

    #66
    def is_six(self, x, y, stone):
        for i in range(4):
            cnt = self.get_stone_count(x, y, stone, i)
            if cnt > 5:
                return True
        return False

    #오목 확인
    def is_five(self, x, y, stone):
        for i in range(4):
            cnt = self.get_stone_count(x, y, stone, i)
            if cnt == 5:
                return True
        return False

    #빈 공간 찾아서 포인트 넘기는 함수
    def find_empty_point(self, x, y, stone, direction):
        dx, dy = self.get_xy(direction)
        while True:
            x, y = x + dx, y + dy
            if self.is_invalid(x, y) or self.board[y][x] != stone:
                break
        if not self.is_invalid(x, y) and self.board[y][x] == empty:
            return x, y
        else:
            return None

    #열린 3
    def open_three(self, x, y, stone, direction):
        for i in range(2):
            coord = self.find_empty_point(x, y, stone, direction * 2 + i)
            if coord:
                dx, dy = coord
                self.set_stone(dx, dy, stone)
                if 1 == self.open_four(dx, dy, stone, direction):
                    if not self.forbidden_point(dx, dy, stone):
                        self.set_stone(dx, dy, empty)
                        return True
                self.set_stone(dx, dy, empty)
        return False

    #열린 4
    def open_four(self, x, y, stone, direction):
        if self.is_five(x, y, stone):
            return False
        cnt = 0
        for i in range(2):
            coord = self.find_empty_point(x, y, stone, direction * 2 + i)
            if coord:
                if self.five(coord[0], coord[1], stone, direction):
                    cnt += 1
        if cnt == 2:
            if 4 == self.get_stone_count(x, y, stone, direction):
                cnt = 1
        else: cnt = 0
        return cnt

    #4 검사
    def four(self, x, y, stone, direction):
        for i in range(2):
            coord = self.find_empty_point(x, y, stone, direction * 2 + i)
            if coord:
                if self.five(coord[0], coord[1], stone, direction):
                    return True
        return False

    #열린 4나 4를 검사할 때 그 방향에 오목 되는지 확인
    def five(self, x, y, stone, direction):
        if 5 == self.get_stone_count(x, y, stone, direction):
            return True
        return False

    #33
    def double_three(self, x, y, stone):
        cnt = 0
        self.set_stone(x, y, stone)
        for i in range(4):
            if self.open_three(x, y, stone, i):
                cnt += 1
        self.set_stone(x, y, empty)
        if cnt >= 2:
            print("double three")
            return True
        return False

    #44
    def double_four(self, x, y, stone):
        cnt = 0
        self.set_stone(x, y, stone)
        for i in range(4):
            if self.open_four(x, y, stone, i) == 2:
                cnt += 2
            elif self.four(x, y, stone, i):
                cnt += 1
        self.set_stone(x, y, empty)
        if cnt >= 2:
            print("double four")
            return True
        return False

    #금수 자리 좌표 체크
    def forbidden_point(self, x, y, stone):
        if self.is_five(x, y, stone):
            return False
        elif self.is_six(x, y, stone):
            print("overline")
            return True
        elif self.double_three(x, y, stone) or self.double_four(x, y, stone):
            return True
        return False

    #금수 자리 좌표 넘기는 함수
    def get_forbidden_points(self, stone):
        coords = []
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x]:
                    continue
                if self.forbidden_point(x, y, stone):
                    coords.append((x, y))
        return coords

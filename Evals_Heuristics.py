"""evaluation function definitions and heuristics"""
from copy import deepcopy

BOARD_SIZE = 3


# get an empty board
def initialize_board():
    current_board = []
    index_x = 0
    while index_x < BOARD_SIZE:
        col = [0]*BOARD_SIZE
        current_board.append(col)
        index_x += 1
    return current_board


# get next level of boards
def get_next_level(board, c_player):
    all_poss = []
    index_y = 0
    while index_y < BOARD_SIZE:
        index_x = 0
        while index_x < BOARD_SIZE:
            if board[index_x][index_y] == 0:
                imaginary_board = deepcopy(board)
                imaginary_board[index_x][index_y] = c_player
                all_poss.append(imaginary_board)
            index_x += 1
        index_y += 1
    return all_poss


def link_top_left(board, stone, already_linked):

    return Link([], "open")


def link_top_right(board, stone, already_linked):
    return Link([], "open")


def link_horizontal(board, stone, already_linked):
    return Link([], "open")


def link_vertical(board, stone, already_linked):
    return Link([], "open")


# get a list of links given a board and a stone
def get_links(board, stone, already_linked):
    links = []
    c_player = stone.player

    if board[stone.x - 1][stone.y + 1] == c_player or board[stone.x + 1][stone.y - 1] == c_player:
        # top left diagonal
        link = link_top_left(board, stone, already_linked)
        if not link.len == 0:
            links.append(link)
    if board[stone.x][stone.y + 1] == c_player or board[stone.x][stone.y - 1] == c_player:
        # vertical
        link = link_vertical(board, stone, already_linked)
        if not link.len == 0:
            links.append(link)
    if board[stone.x + 1][stone.y + 1] == c_player or board[stone.x - 1][stone.y - 1] == c_player:
        # top right diagonal
        link = link_top_right(board, stone, already_linked)
        if not link.len == 0:
            links.append(link)
    if board[stone.x + 1][stone.y] == c_player or board[stone.x - 1][stone.y] == c_player:
        # horizontal
        link = link_horizontal(board, stone, already_linked)
        if not link.len == 0:
            links.append(link)

    return links


def evaluate_value(board, c_player):
    o_player = 1
    if c_player == 1:
        o_player = 2

    # list of links for current player
    evaluated_c_player_stones = []
    # list of links for other player
    evaluated_o_player_stones = []

    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0

    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    y5 = 0

    o1 = 0
    o2 = 0
    o3 = 0
    o4 = 0
    o5 = 0

    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0

    index_x = 0
    while index_x < BOARD_SIZE:
        index_y = 0
        while index_y < BOARD_SIZE:
            if board[index_x][index_y] == c_player:
                links = get_links(board, Stone(index_x, index_y, c_player), evaluated_c_player_stones)
                for link in links:
                    if link.len == 1:
                        if link.type == "open":
                            x1 += 1
                        else:
                            y1 += 1
                    elif link.len == 2:
                        if link.type == "open":
                            x2 += 1
                        else:
                            y2 += 1
                    elif link.len == 3:
                        if link.type == "open":
                            x3 += 1
                        else:
                            y3 += 1
                    elif link.len == 4:
                        if link.type == "open":
                            x4 += 1
                        else:
                            y4 += 1
                    elif link.len == 5:
                        if link.type == "open":
                            x5 += 1
                        else:
                            y5 += 1
            elif board[index_x][index_y] == o_player:
                links = get_links(board, Stone(index_x, index_y, o_player), evaluated_o_player_stones)
                for link in links:
                    if link.len == 1:
                        if link.type == "open":
                            o1 += 1
                        else:
                            p1 += 1
                    elif link.len == 2:
                        if link.type == "open":
                            o2 += 1
                        else:
                            p2 += 1
                    elif link.len == 3:
                        if link.type == "open":
                            o3 += 1
                        else:
                            p3 += 1
                    elif link.len == 4:
                        if link.type == "open":
                            o4 += 1
                        else:
                            p4 += 1
                    elif link.len == 5:
                        if link.type == "open":
                            o5 += 1
                        else:
                            p5 += 1
            index_y += 1
        index_x += 1

    return 3 * (x1 + 3*x2 + 12*x3 + 60*x4 + 1000*x5) + (y1 + 3*y2 + 9*y3 + 50*y4 + 1000*y5) \
        - 2 * (3*(o1 + 3*o2 + 12*o3 + 60*o4 + 1000*o5) + (p1 + 3*p2 + 9*p3 + 50*p4 + 1000*p5))


class Stone:
    def __init__(self, x_pos, y_pos, player):
        self.x = x_pos
        self.y = y_pos
        self.player = player

    def __str__(self):
        return "[" + str(self.x) \
               + "," + str(self.y) \
               + "," + str(self.player) \
               + "]"

    def __eq__(self, other):
        if self.x == other.x \
                and self.y == other.y \
                and self.player == other.player:
            return True
        else:
            return False


class Link:
    def __init__(self, list_of_stone, link_type):
        self.stones = list_of_stone
        self.type = link_type
        self.len = len(self.stones)

    def __eq__(self, other):
        if self.len != other.len:
            return False

        for stone in self.stones:
            if self.stones.count(stone) != other.stones.count(stone):
                return False

        return True


new_board = initialize_board()
new_board[1][1] = 1
new_board[2][2] = 2
poss = get_next_level(new_board, 1)
print evaluate_value(poss[0], 1)
# print all possibilities

"""
for one_poss in poss:
    y = BOARD_SIZE - 1
    while y >= 0:
        x = 0
        row = []
        while x < BOARD_SIZE:
            row.append(one_poss[x][y])
            x += 1
        print row
        y -= 1
    print "\n"
"""
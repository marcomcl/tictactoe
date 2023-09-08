import random
from constants import constants as cns

field = []
size = 3


def choose_size():
    global size, field

    in_value = input(cns.CHOOSE_SIZE)
    print(cns.NEW_LINE)

    if not in_value:
        size = 3
    else:
        try:
            size = int(in_value)

        except ValueError:
            print(cns.CHOOSE_SIZE_ERROR)
            size = 3

    field = [[""] * size for i in range(0, size)]


def choose_characters():

    characters = ["X", "O"]
    index = random.choice([0, 1])

    player1 = characters[index]
    player2 = characters[(index + 1) % 2]

    print(cns.FRAMING)
    print(cns.FIRST.format(player1))
    print(cns.FRAMING)

    return player1, player2


def print_field():
    print(cns.NEW_LINE)

    for row in field:
        print(row)

    print(cns.NEW_LINE)


def choose_position(player):
    while True:
        pos = input(cns.ENTER_VALUE.format(player, size * size))

        try:
            pos = int(pos) - 1
        except ValueError:
            print(cns.ENTER_VALUE_ERROR_TYPE.format(size * size))
            continue

        if pos < 0 or pos > size * size - 1:
            print(cns.ENTER_VALUE_ERROR_RANGE.format(size * size))
            continue

        x, y = pos // size, pos % size

        if field[x][y]:
            print(cns.ENTER_VALUE_ERROR_NOT_EMPTY)
            continue

        field[x][y] = player

        return x, y


def check_left_diagonal(player):
    for i in range(0, size):
        if field[i][i] != player:
            return False
    return True


def check_right_diagonal(player):
    for i in range(0, size):
        if field[i][size - i - 1] != player:
            return False
    return True


def check_vertical(player, x):
    for i in range(0, size):
        if field[x][i] != player:
            return False
    return True


def check_horizontal(player, y):
    for i in range(0, size):
        if field[i][y] != player:
            return False
    return True


def check_victory(player, x, y):
    vert_horiz = check_vertical(player, x) or check_horizontal(player, y)

    if (x * size + y) % 2 != 0:
        return vert_horiz

    elif x == y:
        return vert_horiz or check_left_diagonal(player)

    elif x + y == size - 1:
        return vert_horiz or check_right_diagonal(player)


def play_move(player):
    x, y = choose_position(player)
    return check_victory(player, x, y)


def new_game():
    choose_size()
    players = choose_characters()
    moves = 0

    while moves < size * size:
        print_field()

        if play_move(players[moves % 2]):
            print_field()
            print(cns.WINNER.format(players[moves % 2]))
            return

        moves += 1

    print_field()
    print(cns.DRAW)


if __name__ == "__main__":
    play_again = "Y"

    while play_again == "Y":
        new_game()
        play_again = input(cns.PLAY_AGAIN)

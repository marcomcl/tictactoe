import random

field = []
size = 3


def choose_size():
    global size, field

    in_value = input("Choose the size of the field (default 3): ")
    print("\n")

    if not in_value:
        size = 3
    else:
        try:
            size = int(in_value)

        except ValueError:
            print("You must insert an INTEGER - Setting the size to the default value")
            size = 3

    field = [[""] * size for i in range(0, size)]


def choose_characters():

    characters = ["X", "O"]
    index = random.choice([0, 1])

    player1 = characters[index]
    player2 = characters[(index + 1) % 2]

    print("*" * 25)
    print(f"{player1} makes the first move!")
    print("*" * 25)

    return player1, player2


def print_field():
    print("\n")

    for row in field:
        print(row)

    print("\n")


def choose_position(player):
    while True:
        pos = input(f"[{player}] Enter an integer between 1 and {size * size}: ")

        try:
            pos = int(pos) - 1
        except ValueError:
            print(f"You must insert an INTEGER between 1 and {size * size}!")
            continue

        if pos < 0 or pos > size * size - 1:
            print(f"You must insert an integer BETWEEN 1 AND {size * size}!")
            continue

        x, y = pos // size, pos % size

        if field[x][y]:
            print("Choose another spot!")
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

    while moves < 9:
        print_field()

        if play_move(players[moves % 2]):
            print_field()
            print(f"{players[moves % 2]} wins!")
            return

        moves += 1

    print_field()
    print("Draw!")


if __name__ == "__main__":
    play_again = "Y"

    while play_again == "Y":
        new_game()
        play_again = input("Would you like to play again? [Y/n]")

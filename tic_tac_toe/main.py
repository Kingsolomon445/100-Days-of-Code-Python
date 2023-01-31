import random

board_tiles = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " ",
]


def display_board(board):
    print("-------------")
    for index, tile in enumerate(board):
        print(f"| {tile}", end=" ")
        if index != 0 and (index + 1) % 3 == 0:
            print("|")
            print("-------------")


def set_moves(move, player):
    global board_tiles
    board_tiles[move - 1] = player


def is_win():
    # CHECKING FOR WINS
    # Checking fot horizontals
    prev = 0
    for idx in (3, 6, 9):
        # checking for position 0-3, 3-6, 6-9 at each iteration
        if all('O' == tile for tile in board_tiles[prev:idx]):
            print("Player 1 wins the Game!")
            return 1
        elif all('X' == tile for tile in board_tiles[prev:idx]):
            print(f"{player_2} wins the Game!")
            return 1
        prev = idx

    # Checking for verticals
    for idx in ([0, 3, 6], [1, 4, 7], [2, 5, 8]):
        if all("O" == board_tiles[tile] for tile in idx):
            print("P[layer 1 wins the Game!")
            return 1
        elif all("X" == board_tiles[tile] for tile in idx):
            print(f"{player_2} wins the Game!")
            return 1

    # Checking for Diagonals
    for idx in ([0, 4, 8], [2, 4, 6]):
        if all("O" == board_tiles[tile] for tile in idx):
            print("Player 1 wins the Game!")
            return 1
        elif all("X" == board_tiles[tile] for tile in idx):
            print(f"{player_2} wins the Game!")
            return 1

    return 0


def player_moves(player):
    global moves_played
    if player == "Computer":
        move = random.randint(1, 9)
        while move in moves_played:
            move = random.randint(1, 9)
    else:
        move = int(input(f"Make your Move({player}): "))
        while True:
            if move in moves_played:
                print("This move have already been played!")
                move = int(input(f"Make your Move({player}): "))
            elif move not in range(1, 10):
                print("Invalid Move!")
                move = int(input(f"Make your Move({player}): "))
            else:
                break
    moves_played.append(move)
    return move


print("Welcome to Tic Tac Toe game!")
print("Make your moves with numbers (1-9) with each number representing the next tile")
moves_played = []
opponent = int(input("Type '0' to play with computer, '1' with another player:  "))
if opponent:
    player_2 = "Player 2"
else:
    player_2 = "Computer"
while len(moves_played) < 9:
    # Since player 1 always starts the move hence when length of moves_played at odd, it represents player 2 moves
    if len(moves_played) % 2 == 0:
        set_moves(player_moves("Player 1"), "O")
        print("Player 1 moved!")
    else:
        set_moves(player_moves(f"{player_2}"), "X")
        print(f"{player_2} moved!")
    display_board(board_tiles)
    if is_win():
        break
    if len(moves_played) == 9:
        print("It's a draw!")

print("Game Ended")

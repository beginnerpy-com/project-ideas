"""Tic Tac Toe

This is a simple game that allows two players to play tic tac toe.
"""


def display_board(board):
    """Print the current state of the board."""
    for i, row in enumerate(board):
        if i != 0:
            print("-+-+-")
        row = "|".join(row)
        print(row)


def ask_player_for_location(player):
    """Ask the player where they would like to use their turn"""
    move = None
    while not move:
        try:
            move = int(input(f"{player} where would you like to go? "))
            if move not in range(1, 10):
                move = None
                raise ValueError
        except ValueError:
            print("Please enter a number from 1-9")
    return move


def player_turn_to_board_location(move):
    """Convert the players move to a board location."""
    move -= 1
    row, column = divmod(move, 3)
    return row, column


def check_valid_move(location, board):
    """Check the players move is valid."""
    row, column = player_turn_to_board_location(location)
    if board[row][column] != " ":
        print("That position is already taken")
        return False
    return True


def player_turn(player, board):
    """Ask player to their turn on the board and return the player who will play next."""
    move = ask_player_for_location(player)
    while not check_valid_move(move, board):
        move = ask_player_for_location(player)
    row, column = player_turn_to_board_location(move)
    board[row][column] = player
    display_board(board)
    return board


def switch_player(player):
    """Switch the player from X to O or vice versa and return the player"""
    players = {"X": "O", "O": "X"}
    return players[player]


def check_for_win(board, player):
    """Check if the game is over."""
    for row in board:
        if all(move == player for move in row):
            return f"{player} is the Winner!"

    for column in zip(*board):
        if all(move == player for move in column):
            return f"{player} is the Winner!"

    if all(board[i][i] == player for i in range(3)):
        return f"{player} is the Winner!"

    if all(board[i][2 - i] == "X" for i in range(3)):
        return f"{player} is the Winner!"

    if all(move != " " for row in board for move in row):
        return "Draw!"

    return None


def introduction():
    print(
        """Welcome to tic tac toe!
To make a move, enter the number corresponding to the location as show below
The board and it's playable positions:
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9\n"""
    )


def play():
    """Play the game"""
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    current_player = "X"
    winner = None

    introduction()
    while not winner:
        board = player_turn(current_player, board)
        winner = check_for_win(board, current_player)
        current_player = switch_player(current_player)
    print(winner)


if __name__ == "__main__":
    play()

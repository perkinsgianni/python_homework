# Task 6: More on Classes

# declare exception class for tic tac toe
class TictactoeException(Exception):
    # initialize exception method with self, message params
    def __init__(self, message):
        # store message
        self.message = message
        # call __init__ method of superclass
        super().__init__(message)

class Board():
    # class var of valid game moves
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    # initialize board
    def __init__(self):
        # create 3x3 list of lists with empty spaces
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]

        # track curr player
        self.turn = "X"

    # convert board to str
    def __str__(self):
        # initialize empty list for board rows
        lines = []

        # construct and append the top row
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")

        # append horizontal divider
        lines.append("-----------\n")

        # construct and append the middle row
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")

        # append horizontal divider
        lines.append("-----------\n")

        # construct and append the bottom row
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")

        # join all rows
        return "".join(lines)

    def move(self, move_string):
    # raise exception if input string is not valid move
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        # get index of move position
        move_index = Board.valid_moves.index(move_string)

        # calculate board row index
        row = move_index // 3

        # calculate board column index
        column = move_index % 3

        # raise exception if targeted board space is filled
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        # assign curr player's token to calculated board position
        self.board_array[row][column] = self.turn

        # alternate turns between players
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        # assume board is full, game is tied (cat's game)
        cat = True

        # iterate through board rows to look for empty spaces
        for i in range(3):
            # iterate through board columns to look for empty spaces
            for j in range(3):
                # check if curr space is empty
                if self.board_array[i][j] == " ":
                    # indicate empty space
                    cat = False
                else:
                    # proceed to next column
                    continue
                # exit column loop
                break
            else:
                # proceed to next row
                continue
            # exit row loop
            break

        # return tie game status if no empty spaces exist
        if (cat):
            return (True, "Cat's Game.")

        # indicate win status as false
        win = False

        # iterate through rows to check for win
        for i in range(3):
            # check if first space of curr row is filled
            if self.board_array[i][0] != " ":
                # check if all spaces in curr row match
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    # indicate as win
                    win = True
                    # exit row
                    break

        if not win:
            # iterate through columns to check for win
            for i in range(3):
                # check if first space of curr column is filled
                if self.board_array[0][i] != " ":
                    # check if all spaces in curr column match
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        # indicate as win
                        win = True
                        # exit column
                        break

        if not win:
            # check if center space is filled
            if self.board_array[1][1] != " ":
                # check if top-left to bottom-right diagonal matches
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    # indicate as win
                    win = True
                # check if top-right to bottom-left diagonal matches
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    # indicate as win
                    win = True

        if not win:
            # check if "X" is curr player
            if self.turn == "X":
                # return false for game over, announce player X's turn
                return (False, "X's turn.")
            else:
                # return false for game over, announce player O's turn
                return (False, "O's turn.")
        else:
            # check if upcoming turn switched to player O
            if self.turn == "O":
               #  return true for game over and declare player X the winner
                return (True, "X wins!")
            else:
                # return true for game over and declare player O the winner
                return (True, "O wins!")

# start new game
game_board = Board()

# indicate game status
game_over, status_message = game_board.whats_next()

# progress through game until win or tie
while not game_over:
    # print curr iteration of board
    print(game_board)
    # display curr plater
    print(status_message)
    # prompt curr player to input their move
    user_move = input("Enter your move: ")
    
    try:
        # process curr player's move
        game_board.move(user_move)
    except TictactoeException as error:
        # catch errors
        print(f"\nInvalid action: {error.message}\n")
        # skip turn update and prompt curr player again
        continue

    # update game status
    game_over, status_message = game_board.whats_next()

# print final iteration of board
print(game_board)
# display outcome message to user
print(status_message)

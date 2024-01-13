##                   ##
##    TIC TAC TOE    ##
##                   ##
#######################

# This is some python practice for me outside of the data science realm. I want to build my familiarity and
# comfortability with python. The majority of this code was created simply by following the tutorial by Code
# Coach from youtube. This can be found here: https://www.youtube.com/watch?v=dK6gJw4-NCo

# In his code, he creates a simple tic tac toe game in python and also then includes a computer player that 
# makes moves by sampling random values from a uniform distribution.

# I have not incorporated this computer element in yet. However, in addition to his code, I have built on
# extra features for practice. I added the ability to play repeat games. I also included a score keeping
# component that tracks scores for Player 1 and Player 2. For simplicity, Player 1 is always "X" and the
# first turn will always alternate between X and 0s.

# Creating the board:
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

## Empty board for resetting the game:
empty_board = board.copy()

##Setting up the current player, winner, and score tracker.
current_player = "X"
first_move = "X"
winner = None
p1_score = 0
p2_score = 0

gameRunning = True

#Print Board Function
def printBoard(board):
    print(board[0]+ "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3]+ "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6]+ "|" + board[7] + "|" + board[8])

# Players make the moves
def playerInput(board):
    printBoard(board)
    if current_player == "X":
        inp = int(input('Player 1 Move: '))
    else:
        inp = int(input('Player 2 Move: '))
    if inp >= 1 and inp <= 10 and board[inp - 1] == "-":
        board[inp-1] = current_player
    else:
        print("Not a valid move")

#Checking if there is a winner or not
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[3]
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[6]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[3]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board and not winner:
        print("Tie Game")
        printBoard(board)
        print("Scores:")
        print(f"Player 1: {p1_score}")
        print(f"Player 2: {p2_score}")
        playAgain()


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        global gameRunning
        global p1_score, p2_score
        gameRunning = False
        
        if winner == "X":
            p1_score += 1
            print(f'The winner is Player 1')
        else:
            p2_score += 1
            print(f'The winner is Player 2')
        
        printBoard(board)
        print("Scores:")
        print(f"Player 1: {p1_score}")
        print(f"Player 2: {p2_score}")
        playAgain()

#Switching players between moves
def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

#Players choose whether to continue playing or to stop
def playAgain():
    global gameRunning, board, first_move, current_player
    print("Enter 1 to play again. Enter 0 to quit.")
    newGame = int(input('New Game? '))
    if newGame == 1:
        board = empty_board.copy()
        gameRunning = True
        first_move = "O" if first_move == "X" else "X"
        current_player = first_move 

    if newGame == 0:
        print("Final Scores:")
        print(f"Player 1: {p1_score}")
        print(f"Player 2: {p2_score}")
        gameRunning = False
        

#Running the actual game 
while gameRunning:
    print("Player 1 is X and Player 2 is O")
    playerInput(board)
    switchPlayer()
    checkWin()
    checkTie(board)


##                   ##
##    TIC TAC TOE    ##
##                   ##
#######################

# This is some python practice for me outside of the data science realm. I want to build my familiarity and
# comfortability with python. The majority of this code was created simply by following the tutorial by Code
# Coach from youtube. This can be found here: https://www.youtube.com/watch?v=dK6gJw4-NCo

# In this code, I adapt his code to create a computer to play against. Other fixes I made is that I added a
# double check function before exiting the game. I also fixed the problem where entering an invalid move
# doesn't skip your turn.

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
double_check = False

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
        print("Please pick an open square")
        playerInput(board)

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
         
        print("Scores:")
        print(f"Player: {p1_score}")
        print(f"Computer: {p2_score}")
        playAgain()

#Switching players between moves
def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

import random 

def computerMove(board):
    while current_player == "O":
        move = random.randint(0,8)
        if board[move] == "-":
            board[move] = "O"
            switchPlayer()

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
    else:
        exitGame()

def exitGame():
    global double_check
    if double_check == False:
        check = int(input('Are you sure? Enter 1 to continue: '))
        if check == 1:
            double_check = True
        else:
            playAgain()
    if double_check == True:
        print("Final Scores:")
        print(f"Player: {p1_score}")
        print(f"Computer: {p2_score}")
        gameRunning = False

while gameRunning:
    print("Player 1 is X and Computer is O")
    playerInput(board)
    switchPlayer()
    checkWin()
    checkTie(board)
    if gameRunning == False:
        break
    else:
        computerMove(board)
        checkWin()
        checkTie(board)

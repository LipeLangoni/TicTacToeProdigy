# Hi, my name is Felipe Langoni and this is my first real code.
import random
from TicTacToe import *

# IA function to play the game
def engine(board):
        o = 0

        # Manually compare all sequencies possible, and score in the third one to win the geme, or to stop the oponnent.
        # We use "and board[i][j] == blank" to make sure that the move will just be done if the last square of the sequence is empty, otherwise it will try to score twice in the same square.

        while(o<5):
            if (board[0][0] == board[0][1] and board[0][0] == "O" and board[0][2] == blank):
                board[0][2] = "O"
                break
            elif board[0][0] == board[1][0] and board[0][0] == "O" and board[2][0] == blank:
                board[2][0] = "O"
                break
            elif board[0][1] == board[1][1] and board[0][1] == "O" and board[2][1] == blank:
                board[2][1] = "O"
                break
            elif board[0][2] == board[1][2] and board[0][2] == "O" and board[2][2] == blank:
                board[2][2] = "O"
                break
            elif board[1][0] == board[1][1] and board[1][0] =="O" and board[1][2] == blank:
                board[1][2] = "O"
                break
            elif board[2][0] == board[2][1] and board[2][0] =="O" and board[2][2] == blank:
                board[2][2] = "O"
                break
            elif board[0][0] == board[1][1] and board[0][0] == "O" and board[2][2] == blank:
                board[2][2] = "O"
                break
            elif board[0][2] == board[1][1] and board[0][2] == "O" and board[2][0] == blank:
                board[2][0] = "O"
                break
            

            if (board[0][0] == board[0][1] and board[0][0] == "X" and board[0][2] == blank):
                board[0][2] = "O"
                break
            elif board[0][0] == board[1][0] and board[0][0] == "X" and board[2][0] == blank:
                board[2][0] = "O"
                break
            elif board[0][1] == board[1][1] and board[0][1] == "X" and board[2][1] == blank:
                board[2][1] = "O"
                break
            elif board[0][2] == board[1][2] and board[0][2] == "X" and board[2][2] == blank:
                board[2][2] = "O"
                break
            elif board[1][0] == board[1][1] and board[1][0] =="X" and board[1][2] == blank:
                board[1][2] = "O"
                break
            elif board[2][0] == board[2][1] and board[2][0] =="X" and board[2][2] == blank:
                board[2][2] = "O"
                break
            elif board[0][0] == board[1][1] and board[0][0] == "X" and board[2][2] == blank:
                board[2][2] = "O"
                break
            elif board[0][2] == board[1][1] and board[0][2] == "X" and board[2][0] == blank:
                board[2][0] = "O"
                break
            
            # If none of above cases are found, we create a list using "append" method to save all the empty positions.
            # This list contain lists wich contain the indexes of empty positions 
            # We than choose a position of the list and make it
            else:
                positions = []
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == blank:
                            positions.append([i,j])
                print(positions)
                move = positions[0]
                i = move[0]
                j = move[1]
                board[i][j] = "O"
                break
    
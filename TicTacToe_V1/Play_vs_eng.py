# Hi, my name is Felipe Langoni and this is my first real code.
from TicTacToe import *
from Engine import engine
import random

# This function is exactly the same, but the difference is that instead of calling player2 function, we call engine function.
def __main(board):

    winner = winnerchecker(board)

    while(not winner):
        i = 0
        j = 0
        n = 0
        while(n<10):
            i = moveinput("Enter row position:")
            j = moveinput("Enter column position:")
            if validatemove(board,i,j):
                player1(board,i,j)
                break
            else:
                print("Already Ocupped")
            n+=1
        winner = winnerchecker(board)
        print("The Winner is:", winner)
        if winner:
            printboard(board,i,j)
            break
        engine(board)
        printboard(board,i,j)
        winner = winnerchecker(board)
        print("The Winner is:", winner)
__main(board)
        

        
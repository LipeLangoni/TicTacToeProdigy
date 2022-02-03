# Hi, my name is Felipe Langoni and this is my first real code.

from TicTacToe import *

def __main__(board):
    
    # Function to check if one of the players won the game
    winner = winnerchecker(board)
    
    #while: the code will run until this function finds a winner
    while (not winner):
        v = 0 
        i = 0
        j = 0
        while (v != 5):
            i = moveinput(("Digite o valor de i"))
            j = moveinput(("Digite o valor de j"))

            # if validatemove function returns True, player1 makes his move
            if validatemove(board,i,j):
                player1(board,i,j)
                break
            else:
                print("Already ocupped")
            v += 1
        winner = winnerchecker(board)
        printboard(board,i,j)
        #display current board state
        print("The Winner is:", winner)

        #break method if winner, otherwise it will allow second player to move eventhought player1 already won
        if winner:
            break
        
        #same thing to the other player
        while (v != 5):
            i = moveinput(("Digite o valor de i"))
            j = moveinput(("Digite o valor de j"))

            if validatemove(board,i,j):
                player2(board,i,j)
                break
            else:
                print("Already ocupped")
            printboard(board,i,j)
            v += 1
        winner = winnerchecker(board)
        printboard(board,i,j)
        print("The Winner is:", winner)
__main__(board)
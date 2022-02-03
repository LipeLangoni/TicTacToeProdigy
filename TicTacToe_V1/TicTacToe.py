# Hi, my name is Felipe Langoni and this is my first real code.

#First, we create a variable which contains a empty string
blank = ""

#Than, we create a array with tree arrays inside, each one with tree positions (3x3)
board = [
        [blank,blank,blank],
        [blank,blank,blank],
        [blank,blank,blank],
    ]

# Player functions, player1 will return "X" in the given position, and player2 "O"

def player1(board,i,j):
    board[i][j] = "X"

def player2(board,i,j):
    board[i][j] = "O"

# This function will display the board in a better format

def printboard(board,i,j):
    print(f' {board[0][0]} '+'|'+f' {board[0][1]} '+'|'+f' {board[0][2]} ')
    print('---'+'|'+'---'+'|'+'---')
    print(f' {board[1][0]} '+'|'+f' {board[1][1]} '+'|'+f' {board[1][2]} ')
    print('---'+'|'+'---'+'|'+'---')
    print(f' {board[2][0]} '+'|'+f' {board[2][1]} '+'|'+f' {board[2][2]} ')

    
# if choosen position is equal to a empty string, this move is valid
def validatemove(board,i,j):
    if board[i][j] == blank:
        return True
    else:
        return False


# this fucntion receives user input and convert the indexes to be easier input the position

def moveinput(m):
    p = int(input(m))
    
    if (p >=1 and p<=3):
        return p-1
    else:
        "Invalid Value"
        
        
# This function manually checks for all the possible "tree in a sequence" combinations to determine a winner.

def winnerchecker(board):
   
    if board[0][0] == "X" and board[0][1] =="X" and board[0][2] =="X":
        return  board[0][0]
        
    elif board[1][0] == "X" and board[1][1] =="X" and board[1][2] =="X":
        return board[1][0]
       
    elif board[2][0] == "X" and board[2][1] =="X" and board[2][2] =="X":
        return  board[2][0]
        
    elif board[0][0] == "X" and board[1][0] =="X" and board[2][0] =="X":
        return board[0][0]
        
    elif board[0][1] == "X" and board[1][1] =="X" and board[2][1] =="X":
        return  board[0][1]
        
    elif board[0][2] == "X" and board[1][2] =="X" and board[2][2] =="X":
        return board[0][2]
        
    elif board[0][0] == "X" and board[1][1] =="X" and board[2][2] =="X":
        return board[0][0]
        
    elif board[0][2] == "X" and board[1][1] =="X" and board[2][0] =="X":
        return board[0][2]
    

    
    if board[0][0] == "O" and board[0][1] =="O" and board[0][2] =="O":
        return board[0][0]
        
    elif board[1][0] == "O" and board[1][1] =="O" and board[1][2] =="O":
        return board[1][0]
       
    elif board[2][0] == "O" and board[2][1] =="O" and board[2][2] =="O":
        return board[2][0]
        
    elif board[0][0] == "O" and board[1][0] =="O" and board[2][0] =="O":
        return board[0][0]
        
    elif board[0][1] == "O" and board[1][1] =="O" and board[2][1] =="O":
        return board[0][1]
        
    elif board[0][2] == "O" and board[1][2] =="O" and board[2][2] =="O":
        return board[0][2]
        
    elif board[0][0] == "O" and board[1][1] =="O" and board[2][2] =="O":
        return  board[0][0]
        
    elif board[0][2] == "O" and board[1][1] =="O" and board[2][0] =="O":
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if(board[i][j] == blank):
                return False
    return "EMPATE"
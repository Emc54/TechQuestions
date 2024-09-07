"""
The N–queens puzzle is the problem of placing N chess queens on an N × N 
chessboard so that no two queens threaten each other. Thus, the solution 
requires that no two queens share the same row, column, or diagonal.

Solutions for the N-queens problem:

To be confirmed with https://lyndenlea.uk/nqueens/

Boards to try:

4x4, 5x5, 6x6, 7x7, 8x8


"""


"""
01  02  03  04  05
06  07  08  09  10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25

"""


N = 8 

## for row in board:
##     for tile in row:
        ## check for another queen in the way
        ## if nothing, place
        ## if can't place move on to next spot
    ## if can't place anywhere in the row we need to backtrack

board=[["-"]*N for _ in range(N)]

def solve(board, row=0):

    if row == len(board):
        for idx,row in enumerate(board):
            print(row)
            if idx%N==N-1: print("")
        return

    for i in range(len(board)):

        if check_queen(board,row,i):
            
            board[row][i] = "Q"
            
            solve(board, row+1)

            board[row][i] = "-"

def check_queen(board,row,tile):

#check the column upwards
    for i in range(row):
        if board[i][tile] == "Q":
            return False

#check the diagonals

    (n,m) = (row, tile)

### Top Left
    while n >= 0 and m >= 0:
        if board[n][m] == "Q":
            return False
        n= n-1
        m= m-1

### Top Right

    (n,m) = (row, tile)
    while n >= 0 and m<len(board):
        if board[n][m] == "Q":
            return False
        n=n-1
        m=m+1

    return True




solve(board)


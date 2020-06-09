'''
https://www.codewars.com/kata/525caa5c1bf619d28c000335

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? 
Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X",
or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]

We want our function to return:

    -1 if the board is not yet finished (there are empty spots),
    1 if "X" won,
    2 if "O" won,
    0 if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
'''


def row(board):
    rows = [board[i,:] for i in range(3)]
    return rows

def column(board):
    columns = [board[:,i] for i in range(3)]
    return columns

def diagonal(board):
    diagonals = [[board[0][0], board[1][1], board[2][2]],[board[0][2], board[1][1], board[2][0]]]
    return diagonals
                
def is_solved(aboard):
    import numpy as np
    i = 0
    board = np.array(aboard)
    
    rows = row(board)
    columns = column(board)
    diagonals = diagonal(board)
    
    while(i!=8):
        for analysis in np.vstack((rows,columns,diagonals)):
            if(len(np.unique(analysis)) == 1 and np.unique(analysis) != 0):
                if(np.unique(analysis) == 1):
                    return 1
                elif(np.unique(analysis) == 2):
                    return 2
            i+=1
    if(i==8):
        i=0
        for analysis in np.vstack((rows,columns,diagonals)):
            for number in analysis:
                if number == 0:
                    return -1
                i+=1
                if(i==24):
                    return 0

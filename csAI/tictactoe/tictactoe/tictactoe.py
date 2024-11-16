"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #probably call teh if terminal function to cut it off early
    #otherwise count up all the xs or os and then %
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #NOTE: starts from 0 (i.e., [0,1,2])
    #i is y
    #j is x
    #probably call teh if terminal function to cut it off early
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if won("X", board):
        return True
    if won("O", board):
        return True
    elif tied(board):
        return True
    return False

def won(input, board):
    """
    checks if input (e.g., X or O) won , returns true if so
    else returns false
    """
    if horus(input, board):
        return True
    elif vert(input, board):
        return True
    elif dag(input,board):
        return True
    return False
    #get to it 

def horus(input, board):
    """
    checks if input (e.g., X or O) won horizontally, returns true if so
    else returns false
    """
    for _ in board:
        if _ == [input,input,input]:
            return True
    return False

def vert(input, board):
    """
    checks if input (e.g., X or O) won verticaly, returns true if so
    else returns false
    """
    col0 = []
    col1 = list()
    col2 = list()
    for _ in board:
        for oopsies in range(len(_)):
            if oopsies == 0:
                col0.append(_[oopsies])
            elif oopsies == 1:
                col1.append(_[oopsies])
            elif oopsies == 2:
                col2.append(_[oopsies])
    for crabunkula in range(3):
        if col0 == [input,input, input]:
            return True
        elif col1 [input,input, input]:
            return True
        elif col2 [input,input, input]:
            return True
    return False

def dag(input,board):
    """
    checks if input (e.g., X or O) won diagonally, returns true if so
    else returns false
    """

    #lr represents left to right and vice verse
    lr = list()
    rl = list()

    for _ in range(3):
        lr.append(board[_][_])
    for _ in range(3):
        bingus = 2-_
        rl.append(board[_][bingus])
    if lr == [input,input, input]:
        return True
    elif rl [input,input, input]:
        return True
    return False



def tied(board):
    """
    checks if board is full, i.e. tied, returns True if so False if not
    """
    for _ in board:
        for oopsies in _ :
            if oopsies == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

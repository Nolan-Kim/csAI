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
    mrX = 0
    mrO = 0
    for _ in board:
        for oopsies in _:
            if oopsies == X:
                mrX += 1
            elif oopsies == O:
                mrO += 1
                #Do I need this maybe just count x's? the inefficient way I'm doin it ye
    if mrX == mrO:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #NOTE: starts from 0 (i.e., [0,1,2])
    #i is y
    #j is x
    #scans for emptys probably?
    #probably call teh if terminal function to cut it off early terminal function might be less efficient, maybe
    posseActions = set()
    for _ in range(len(board)):
        for oopsies in range(len(board[_])):
            if board[_][oopsies] == EMPTY:
                posseActions.add((_,oopsies))
    return posseActions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = board
    newBoard[action[1]][action[0]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if won(X, board):
        return X
    elif won(O, board):
        return O
    else:
        return None

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
    if col0 == [input,input, input]:
        return True
    elif col1 == [input,input, input]:
        return True
    elif col2 == [input,input, input]:
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
    elif rl == [input,input, input]:
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
    if won(X, board):
        return 1
    elif won(O, board):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print("just ran")
    #x util is 1
    #O util is -1
    #if terminal returns the utility if not add to frontier?
    #gonna create a new class and stuff
    # class named mrGarvey takes parent and board and action?
    #?? what am I doing what is mrGarvey
    #found out mrGarvey is used for parent node, so I know when the initial board is bad

    #psuedo code starts now
    #gets board, checks if inital board is terminal if so end it
    #if not check if terminal and who won
    #god I'm too tired for this, maybe burn this and start again?
    #start from beginning if terminal needs to return None
    #basically if X's turn then its O's turn

    #construction of possible board
    #[[EMPTY,EMPTY,X],
     #[EMPTY, O, EMPTY],
     #[X, EMPTY, EMPTY]]
    #best move is (1,0) or any blocking move (e.g., (0,1)
    
    #if initial board terminal return None
    #if not terminal return bestMove(board)

    #best move is the best move of the next person

    #how to calc

    #probably by using a terminal function

    if terminal(board):
        return False

    if player(board) == X:
        #x's turn
        #maximize
        bestUtil = float("-inf")
        bestMove = ()
        for _ in actions(board):
            newBoard = board
            print(_[0])
            print(_[1])
            newBoard[_[0][_[1]]] = X
            crab = minimax(newBoard)
            if crab == None:
                #funcy was terminal
                util = utility(crab)
                if util > bestUtil:
                    bestUtil = util
                    bestMove = _
        return bestMove
    else:
        #O's turn
        #minimize
        bestUtil = float("inf")
        bestMove = ()
        for _ in actions(board):
            newBoard = board
            newBoard[_[0][1]] = O
            crab = minimax(newBoard)
            if crab == None:
                #funcy was terminal
                util = utility(crab)
                if util < bestUtil:
                    bestUtil = util
                    bestMove = _
        return bestMove
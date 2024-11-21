import tictactoe as t

X = "X"
O = "O"
EMPTY = None
emptyBoard =[[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
halfFull = [[X, EMPTY, X],
            [EMPTY, O, EMPTY],
            [EMPTY, O, X]]

def test_dag():
  #diagonal board
  assert t.dag(X,[[X,O,X],
                  [O,X,O],
                  [X,O,X]]) == True
  #board still in progress
  assert t.dag(X, halfFull) == False
  #empty board
  assert t.dag(X, emptyBoard) == False
  #diagonals each individually to isolate if one doesn't work
  assert t.dag(X,[[EMPTY,O,X],
                [O,X,EMPTY],
                [X,O,X]]) == True
  assert t.dag(O,[[O,EMPTY,X],
                [EMPTY,O,EMPTY],
                [X,X,O]]) == True
def test_vert():
  #not verticals
  assert t.vert(X,[[X,O,X],
                  [O,X,O],
                  [X,O,X]]) == False
  #board still in progress
  assert t.vert(X, halfFull) == False
  #empty board
  assert t.vert(X, emptyBoard) == False
  #verticals each column indidivually to islate if one lacks functionality
  assert t.vert(X,[[X,EMPTY,EMPTY],
                  [X,EMPTY,EMPTY],
                  [X,EMPTY,EMPTY]]) == True
  assert t.vert(X,[[EMPTY,X,EMPTY],
                  [EMPTY,X,EMPTY],
                  [EMPTY,X,EMPTY]]) == True
  assert t.vert(O,[[EMPTY,EMPTY,O],
                  [EMPTY,EMPTY,O],
                  [EMPTY,EMPTY,O]]) == True
def test_horiz():
  assert t.horus(X, [[X,O,X],
                    [O,X,O],
                    [X,O,X]]) == False
  #board still in progress
  assert t.horus(X, halfFull) == False
  #empty board
  assert t.horus(X, emptyBoard) == False
  #horizzises each row indidivually to islate if one lacks functionality
  assert t.horus(X, [[X,X,X],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY]])
  assert t.horus(X, [[EMPTY, EMPTY, EMPTY],
                     [X,X,X],
                    [EMPTY, EMPTY, EMPTY]])
  assert t.horus(O, [[EMPTY, EMPTY, EMPTY], 
                    [EMPTY, EMPTY, EMPTY],
                    [O,O,O]])
def test_terminal():
  assert t.terminal([[X,O,X],
                    [O,X,O],
                    [X,O,X]]) == True
def test_won():
  #tests if it recognizes terminal states
  assert t.won(X, [[X,O,X],
                  [O,X,O],
                  [X,O,X]]) == True
  assert t.won(O, [[X,O,X],
                  [O,X,O],
                  [X,O,X]]) == False
def test_tied():
  assert t.tied([[X,O,X],
                [O,X,O],
                [X,O,X]]) == True
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
  #I think this works because this runs after the checks for if x wins
  #this just checks if all spaces are filled
  assert t.tied([[X,O,X],
                [O,X,O],
                [X,O,X]]) == True
  assert t.tied([[O,O,X],
                [X,X,O],
                [O,X,X]]) == True
def test_player():
  assert t.player(emptyBoard) == X
  assert t.player([[X, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == O
  assert t.player([[X, O, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == X
  assert t.player([[X, O, X],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == O
  assert t.player([[X, O, X],
                   [O, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == X
  assert t.player([[X, O, X],
                   [O, X, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == O
  assert t.player([[X, O, X],
                   [O, X, O],
                   [EMPTY, EMPTY, EMPTY]]) == X
  assert t.player([[X, O, X],
                   [O, X, O],
                   [X, EMPTY, EMPTY]]) == O
  assert t.player([[X, O, X],
                   [O, X, O],
                   [X, O, EMPTY]]) == X
  #just to check it returns something, technically don't know if it is O but logic reasons so
  assert t.player([[X, O, X],
                   [O, X, O],
                   [X, O, X]]) == O
def test_winner():
  #kind of redundant, cause just won func but still bears test anyways
  assert t.winner([[X,O,X],
                  [O,X,O],
                  [X,O,X]]) == X
  assert t.winner([[X,O,X],
                  [O,O,EMPTY],
                  [X,O,X]]) == O
def test_utility():
  assert t.utility([[X,O,X],
                  [O,X,O],
                  [X,O,X]]) == 1
  assert t.utility([[X,O,X],
                  [O,O,EMPTY],
                  [X,O,X]]) == -1
  assert t.utility([[O,O,X],
                    [X,X,O],
                    [O,X,X]]) == 0
def test_actions():
  #test a lil moer buddy
  assert t.actions(emptyBoard) == {(0,0),(0,1),(0,2),
                                   (1,0),(1,1),(1,2),
                                   (2,0),(2,1),(2,2)}
  assert t.actions([[X,O,X],
                    [O,EMPTY,EMPTY],
                    [X,O,X]]) == {(1,1),(1,2)}
  assert t.actions([[X, EMPTY, O],
                    [EMPTY, X, EMPTY],
                    [EMPTY, EMPTY, O]]) == {(0,1),(1,0),(1,2),(2,0),(2,1)}
def test_minimax():
  assert t.minimax([[X,O,X],
                    [O,EMPTY,O],
                    [X,O,X]]) == (1,1)
  assert t.minimax([[X,O,EMPTY],
                    [O,EMPTY,EMPTY],
                    [X,O,X]]) == (1,1)
  assert t.minimax([[X, EMPTY, X],
                    [EMPTY, O, EMPTY],
                    [EMPTY, O, X]]) == (0,1)
  assert t.minimax([[X, EMPTY, X],
                    [EMPTY, O, EMPTY],
                    [EMPTY, O, X]]) == (0,1)
  assert t.minimax([[O,O,X],
                    [X,X,O],
                    [O,X,X]]) == None
  assert t.minimax([[EMPTY,EMPTY,X],
                    [EMPTY, O, EMPTY],
                    [X, EMPTY, EMPTY]]) == (1,0)
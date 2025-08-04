import math

# Initialize a 3x3 Tic-Tac-Toe board with empty spaces.
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

Max = 'X'
Min = 'O'
nodes_visited = 0

def print_board(board):
    a = [["⁰","¹","²"],["³","⁴","⁵"],["⁶","⁷","⁸"]]
    for i in range(3):
        print('-------------')
        print('|', end='')
        for j in range(3):
            print(board[i][j], end=f' {a[i][j]}|')
        print()
    print('-------------')

def is_winner(board, player):
    """checks the given player has won or not ., return true , false """
    diag1_check = True
    diag2_check = True
    for i in range(3):
        row_check = True
        col_check = True
        for j in range(3):
            if board[i][j] != player:
                row_check = False
            if board[j][i] != player:
                col_check = False
            if i == j and board[i][j] != player:
                diag1_check = False
            if i + j == 2 and board[i][j] != player:
                diag2_check = False
        if row_check or col_check:
            return True
    if diag1_check or diag2_check:
        return True
    return False

def is_full(board):
    """returns True if the board is full else false"""
    empty_places = 0
    for row in board:
        empty_places += row.count(' ')
    return empty_places == 0

def minimax(board, is_maximizing):
    """ Minimax algorithm to evaluate board positions two option ,set depth level heuristic ,or 
    continue till game end ,return best score  """
    
    # check if anyone is winning or not
    
    # if maximixing  check its best score
    # and call minimizer 
    #  if minimizing check its best score , and call maximizing  .
    
    # do it until someone wins
    global nodes_visited
    nodes_visited += 1
    index = (0,0)
    if is_winner(board, Max):
        return (1, index)
    if is_winner(board, Min):
        return (-1, index)
    if is_full(board):
        return (0, index)
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = Max
                    ss = minimax(board, False)[0]
                    board[i][j] = ' '
                    if ss > best_score:
                        best_score = ss
                        index = (i,j)
        return (best_score, index)
        
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = Min
                    ss = minimax(board, True)[0]
                    board[i][j] = ' '
                    if ss < best_score:
                        best_score = ss
                        index = (i,j)
        return (best_score, index)

def best_move():
    """finds and returns the best move for the AI using the minimax function."""
    # set score negative infinty 
    # call minimax   
    bm = minimax(board, True)
    return bm

def main():
    print_board(board)
    while True:
        print('\n<- Your Turn ->\n')
        s = int(input("Enter Your Next Move [0 to 8]: "))
        if s < 0 or s > 8 or board[s//3][s%3] != ' ':
            print('Invalid Move')
            continue
        else:
            board[s//3][s%3] = Min
        print_board(board)
        if is_winner(board, Min):
            print('User Wins')
            break
        if is_full(board):
            print('DRAW')
            break
        bm = best_move()
        board[bm[1][0]][bm[1][1]] = Max
        print("\n<- AI's Move ->\n")
        print_board(board)
        if is_winner(board, Max):
            print('Ai wins')
            break
        if is_full(board):
            print("DRAW")
            break
    print(nodes_visited)
main()
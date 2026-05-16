#Chapter 7 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter7.html

'''
BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = "||"
BLACK_SQUARE = "  "
'''


STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

def isValidChessBoard(board):
    white_pieces =  {}
    black_pieces = {}
    is_valid = True
    for key, value in board.items():
        #if the board position isn't two characters (i.e a1)
        if len(key) != 2:
            print("Invalid position", key)
            is_valid = False
            continue
        
        #if the piece isn't in one of the columns
        if key[0].lower() not in "abcdefgh":
            print("Invalid column:", key)
            is_valid = False
            continue

        #if the rows isn't a number somehow
        if not key[1].isdigit():
            print("Invalid row:", key)
            is_valid = False
            continue

        #checking if the row is between numbers 1-8 (see comment of the board above)
        if int(key[1]) > 8 or int(key[1]) < 1:
            print("Invalid position:", key)
            is_valid = False
            continue
        
        #if the piece isn't two characters (i.e bK)
        if len(value) != 2:
            print("Invalid piece:", value)
            is_valid = False 
            continue 
        
        #if the piece isn't a black or white piece
        if value[0].lower() not in "bw":
            print("Invalid piece:", value)
            print("Pieces should either be black or white.")
            is_valid = False
            continue

        #if the piece isn't a valid chess piece
        if value[1].upper() not in "RNBQKP":
            print("Invalid piece:", value)
            print("Pieces should only be pawns, knights, bishops, rooks, queens, or kings.")
            is_valid = False
            continue
        
        #adding together the total number of each piece
        if value[0].lower() == "b":
            black_pieces[value[1]] = black_pieces.get(value[1], 0) + 1
        else:
            white_pieces[value[1]] = white_pieces.get(value[1], 0) + 1
            
    #if there are a max of 16 pieces for each player
    if sum(white_pieces.values()) > 16:
        print("Too many white pieces on the board.")
        is_valid = False
    if sum(black_pieces.values()) > 16:
        print("Too many black pieces on the board.")
        is_valid = False

    #if there are more than 8 pawns somehow
    if white_pieces.get('P', 0) > 8:
        print("Too many white pawns. There can be only 8 pawns at most.")
        is_valid = False
    if black_pieces.get('P', 0)> 8:
        print("Too many black pawns. There can be only 8 pawns at most.")
        is_valid = False

    #if there isn't exactly one king for each player
    if white_pieces.get('K', 0) != 1:
        print("White must have exactly one king.")
        is_valid = False

    if black_pieces.get('K', 0) != 1:
        print("Black must have exactly one king.")
        is_valid = False
    return is_valid

isValidChessBoard(STARTING_PIECES)
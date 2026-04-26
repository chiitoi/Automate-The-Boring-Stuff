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
        #if the piece is not in an 8x8 grid
        if len(key) != 2:
            print("Invalid position", key)
            is_valid = False
            continue
        
        if key[0].lower() not in "abcdefgh":
            print("Invalid column:", key)
            is_valid = False
            continue
        if not key[1].isdigit():
            print("Invalid row:", key)
            is_valid = False
            continue
        
        if int(key[1]) > 8 or int(key[1]) < 1:
            print("Invalid position:", key)
            is_valid = False
            continue

        if len(value) != 2:
            print("Invalid piece:", value)
            is_valid = False 
            continue 
        
        if value[0].lower() not in "bw":
            print("Invalid piece:", value)
            print("Pieces should either be black or white.")
            is_valid = False
            continue
        if value[1].upper() not in "RNBQKP":
            print("Invalid piece:", value)
            print("Pieces should only be pawns, knights, bishops, rooks, queens, or kings.")
            is_valid = False
            continue

        if value[0].lower() == "b":
            black_pieces[value[1]] = black_pieces.get(value[1], 0) + 1
        else:
            white_pieces[value[1]] = white_pieces.get(value[1], 0) + 1
            

    if sum(white_pieces.values()) > 16:
        print("Too many white pieces on the board.")
        is_valid = False
    if sum(black_pieces.values()) > 16:
        print("Too many black pieces on the board.")
        is_valid = False

    if white_pieces.get('P', 0) > 8:
        print("Too many white pawns. There can be only 8 pawns at most.")
        is_valid = False
    if black_pieces.get('P', 0)> 8:
        print("Too many black pawns. There can be only 8 pawns at most.")
        is_valid = False

    if white_pieces.get('K', 0) != 1:
        print("White must have exactly one king.")
        is_valid = False

    if black_pieces.get('K', 0) != 1:
        print("Black must have exactly one king.")
        is_valid = False
    return is_valid

isValidChessBoard(STARTING_PIECES)
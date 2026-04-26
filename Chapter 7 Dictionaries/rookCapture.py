def white_rook_can_capture(rook, board):
    rook_col, rook_row = rook[0], rook[1]
    possible_captures = []
    #rooks can only move in column/rows so this checks if there is a position on the board in the same row/column as the rook
    #then it checks if the piece on that position is not white
    for position, piece in board.items():
        pos_col, pos_row = position[0], position[1]
        if (pos_col == rook_col or pos_row == rook_row) and piece[0] != 'w':
            possible_captures.append(position)
       
    return possible_captures

print(white_rook_can_capture('d3', {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'}))
print(white_rook_can_capture('d3', {'d7': 'wQ', 'd2': 'wB', 'f1': 'wP', 'a3': 'wN'}))
print(white_rook_can_capture('d3', {'b3': 'bP', 'f3': 'bN', 'g4': 'wQ', 'd5': 'bK'}))

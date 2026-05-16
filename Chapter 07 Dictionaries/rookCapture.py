#Chapter 7 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter7.html

#Checks if a white rook can capture other pieces on the board
def white_rook_can_capture(rook, board):
    rook_col, rook_row = rook[0], rook[1]
    possible_captures = []

    #Rooks can only move in column/rows so this checks if there is a position on the board in the same row/column as the rook
    #Then it checks if the piece on that position is not white
    for position, piece in board.items():
        pos_col, pos_row = position[0], position[1]
        if (pos_col == rook_col or pos_row == rook_row) and piece[0] != 'w':
            possible_captures.append(position)

    return possible_captures

print(white_rook_can_capture('d3', {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'}))
print(white_rook_can_capture('d3', {'d7': 'wQ', 'd2': 'wB', 'f1': 'wP', 'a3': 'wN'}))
print(white_rook_can_capture('d3', {'b3': 'bP', 'f3': 'bN', 'g4': 'wQ', 'd5': 'bK'}))

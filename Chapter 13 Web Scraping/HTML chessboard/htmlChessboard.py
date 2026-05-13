import random

def get_random_chessboard():
    pieces = 'bP bN bR bB bQ bK wP wN wR wB wQ wK'.split()

    board = {}
    for board_rank in '87654321':
        for board_file in 'abcdefgh':

            if random.randint(1, 6) == 1:
                board[board_file + board_rank] = random.choice(pieces)
    return board

def write_html_chessboard(board):
    unicode_pieces = {
    'wK': '♔', 'wQ': '♕', 'wR': '♖', 'wB': '♗', 'wN': '♘', 'wP': '♙',
    'bK': '♚', 'bQ': '♛', 'bR': '♜', 'bB': '♝', 'bN': '♞', 'bP': '♟'
    }
    # Open an html file for writing the chessboard html:
    with open('chessboard.html', 'w', encoding='utf-8') as file_obj:
        # Start the table element:
        file_obj.write(f'<table border="0">\n')

        write_white_square = True  # Start with a white square.
        font_color = ""
        # Loop over all the rows ("ranks") on the board:
        for board_rank in '87654321':
            # Start the table row element:
            file_obj.write('    <tr>\n')
            # Loop over all the columns ("files") on the board:
            for board_file in 'abcdefgh':
                # Start the table data cell element:
                file_obj.write('    <td style="background: ')

                # Give it a white or black background:
                if write_white_square:
                    file_obj.write('white')
                    font_color = "black"
                else:
                    file_obj.write('black')
                    font_color = "white"

                # Switch square color:
                write_white_square = not write_white_square

                file_obj.write('; width: 60px; height: 60px;">')

                # Write the html for a chess piece image:
                square = board_file + board_rank
                
                if square in board:
                    file_obj.write(f'<center style="color:{font_color}; font-size:2em;">{unicode_pieces[board[square]]}</center>')

                # Finish the table data cell element:
                file_obj.write('</td>\n')
            # Finish the table row element:
            file_obj.write('    </tr>\n')
            # Switch square color for the next row:
            write_white_square = not write_white_square
        # Finish the table element:
        file_obj.write('</table>')

write_html_chessboard(get_random_chessboard())
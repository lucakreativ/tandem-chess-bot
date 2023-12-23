from constantsChess import *

def fenToPosition(fen):
    color = [0] * 64
    piece = [-1] * 64

    reachedEndOfPosition = False
    counter = 63
    i = 0
    while i < len(fen) and reachedEndOfPosition == False:
        if fen[i] == ' ':
            reachedEndOfPosition = True
        elif fen[i] == '/':
            pass
        elif fen[i].isdigit():
            counter -= int(fen[i])
        else:
            if fen[i].isupper():
                color[counter] = WHITE
            else:
                color[counter] = BLACK

            if fen[i].lower() == 'p':
                piece[counter] = PAWN
            elif fen[i].lower() == 'n':
                piece[counter] = KNIGHT
            elif fen[i].lower() == 'b':
                piece[counter] = BISHOP
            elif fen[i].lower() == 'r':
                piece[counter] = ROOK
            elif fen[i].lower() == 'q':
                piece[counter] = QUEEN
            elif fen[i].lower() == 'k':
                piece[counter] = KING
            else:
                print("ERROR: Invalid FEN string")
                return None
            
            counter -= 1

        i += 1
        

    return color, piece
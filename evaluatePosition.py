from constantsChess import *
from boardOperation import *

KING_VALUE = 10000
QUEEN_VALUE = 900
ROOK_VALUE = 500
BISHOP_VALUE = 300
KNIGHT_VALUE = 300
PAWN_VALUE = 100

def evaluate(color, piece, sideToMove=WHITE):
    if sideToMove == WHITE:
        finalBlackorWhite = 1
    else:
        finalBlackorWhite = -1
    materialScore = 0
    for i in range(64):
        if color[i] == WHITE:
            blackOrWhite = 1
        elif color[i] == BLACK:
            blackOrWhite = -1

        if color[i] == EMPTY:
            continue
        elif piece[i] == KING:
            materialScore += blackOrWhite * KING_VALUE
        elif piece[i] == QUEEN:
            materialScore += blackOrWhite * QUEEN_VALUE
        elif piece[i] == ROOK:
            materialScore += blackOrWhite * ROOK_VALUE
        elif piece[i] == BISHOP:
            materialScore += blackOrWhite * BISHOP_VALUE
        elif piece[i] == KNIGHT:
            materialScore += blackOrWhite * KNIGHT_VALUE
        elif piece[i] == PAWN:
            materialScore += blackOrWhite * PAWN_VALUE

    if materialScore == -900:
        printBoard(color, piece)
    return materialScore * finalBlackorWhite
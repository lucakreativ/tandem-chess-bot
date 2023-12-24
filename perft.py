from moveGeneration import moveGeneration
from boardOperation import generateBoard

def perft(color, piece, sideToMove, xSideToMove, depth, enPassantSquare = -2):
    if depth == 0:
        return 1

    moves = moveGeneration(color, piece, sideToMove, xSideToMove, enPassantSquare)
    nodes = 0
    for move in moves:
        color2, piece2 = generateBoard(color, piece, move)
        nodes += perft(color2, piece2, xSideToMove, sideToMove, depth - 1, move[2])

    return nodes
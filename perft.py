from moveGeneration import moveGeneration
from boardOperation import generateBoard

def perft(color, piece, sideToMove, xSideToMove, depth):
    if depth == 0:
        return 1

    moves = moveGeneration(color, piece, sideToMove, xSideToMove)
    nodes = 0
    for move in moves:
        color2, piece2 = generateBoard(color, piece, move)
        nodes += perft(color2, piece2, xSideToMove, sideToMove, depth - 1)
        
    return nodes
from constantsChess import *
from fenToPosition import fenToPosition

def pawnMoveGeneration(color, piece, i, xSideToMove):
    moves = []
    if color[i + 8] == EMPTY:
        moves.append(i + 8)

        if i >= 8 and i <= 15 and color[i + 16] == EMPTY:
            moves.append(i + 16)


    if mailbox[mailbox64[i] + 11] != -1 and color[i + 9] == xSideToMove:
        moves.append(i + 9)
    if mailbox[mailbox64[i] + 9] != -1 and color[i + 11] == xSideToMove:
        moves.append(i + 7)


    return moves

def knightMoveGeneration():
    print("knightMoveGeneration")

    return []

def bishopMoveGeneration():
    print("bishopMoveGeneration")

    return []

def rookMoveGeneration():
    print("rookMoveGeneration")

    return []

def queenMoveGeneration():
    print("queenMoveGeneration")

    return []

def kingMoveGeneration():
    print("kingMoveGeneration")

    return []




def moveGeneration(color, piece, sideToMove, xSideToMove):
    potentialMoves = []
    for i in range(64):
        if color[i] == sideToMove:
            if piece[i] == PAWN:
                potentialMoves += pawnMoveGeneration(color, piece, i, xSideToMove)
            elif piece[i] == KNIGHT:
                potentialMoves += knightMoveGeneration()
            elif piece[i] == BISHOP:
                potentialMoves += bishopMoveGeneration()
            elif piece[i] == ROOK:
                potentialMoves += rookMoveGeneration()
            elif piece[i] == QUEEN:
                potentialMoves += queenMoveGeneration()
            elif piece[i] == KING:
                potentialMoves += kingMoveGeneration()
            else:
                print("ERROR: Invalid piece")
                return None
            
    print(potentialMoves)

def main():
    color, piece = fenToPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    print(color)
    print(piece)
    moveGeneration(color, piece, WHITE, BLACK)

if __name__ == "__main__":
    main()
from constantsChess import *

def pawnMoveGeneration(color, i, xSideToMove):
    moves = []
    if xSideToMove == BLACK:
        if color[i + 8] == EMPTY:
            moves.append((i, i + 8))

            if i >= 8 and i <= 15 and color[i + 16] == EMPTY:
                moves.append((i, i + 16))


        if mailbox[mailbox64[i] + 11] != -1 and color[i + 9] == xSideToMove:
            moves.append((i, i + 9))
        if mailbox[mailbox64[i] + 9] != -1 and color[i + 7] == xSideToMove:
            moves.append((i, i + 7))

    if xSideToMove == WHITE:
        if color[i - 8] == EMPTY:
            moves.append((i, i - 8))

            if i >= 48 and i <= 55 and color[i - 16] == EMPTY:
                moves.append((i, i - 16))

        if mailbox[mailbox64[i] - 11] != -1 and color[i - 9] == xSideToMove:
            moves.append((i, i - 9))
        if mailbox[mailbox64[i] - 9] != -1 and color[i - 7] == xSideToMove:
            moves.append((i, i - 7))

    return moves

def knightMoveGeneration(color, i, sideToMove):
    moves = []
    for offsetMove in offset[1]:
        square = mailbox[mailbox64[i] + offsetMove]
        if square != -1 and color[square] != sideToMove:
            moves.append((i, square))

    return moves

def bishopMoveGeneration(color, i, xSideToMove):
    moves = []
    for offsetMove in offset[2]:
        for j in range(1, 8):
            square = mailbox[mailbox64[i] + offsetMove * j]
            if square == -1:
                break
            elif color[square] == EMPTY:
                moves.append((i, square))
            elif color[square] == xSideToMove:
                moves.append((i, square))
                break
            else:
                break

    return moves

def rookMoveGeneration(color, i, xSideToMove):
    moves = []
    for offsetMove in offset[3]:
        for j in range(1, 8):
            square = mailbox[mailbox64[i] + offsetMove * j]
            if square == -1:
                break
            elif color[square] == EMPTY:
                moves.append((i, square))
            elif color[square] == xSideToMove:
                moves.append((i, square))
                break
            else:
                break

    return moves

def queenMoveGeneration(color, i, xSideToMove):
    moves = []
    for offsetMove in offset[4]:
        for j in range(1, 8):
            square = mailbox[mailbox64[i] + offsetMove * j]
            if square == -1:
                break
            elif color[square] == EMPTY:
                moves.append((i, square))
            elif color[square] == xSideToMove:
                moves.append((i, square))
                break
            else:
                break

    return moves

def kingMoveGeneration(color, i, sideToMove):
    moves = []
    for offsetMove in offset[5]:
        square = mailbox[mailbox64[i] + offsetMove]
        if square != -1 and color[square] != sideToMove:
            moves.append((i, square))

    return moves


def generateBoard(color, piece, move):
    copyColor = color.copy()
    copyPiece = piece.copy()

    copyColor[move[1]] = copyColor[move[0]]
    copyPiece[move[1]] = copyPiece[move[0]]
    copyColor[move[0]] = EMPTY
    copyPiece[move[0]] = -1

    return copyColor, copyPiece


def checkIfMoveIsLegal(color, piece, sideToMove, xSideToMove, move):
    testColor, testPiece = generateBoard(color, piece, move)
    for i in range(64):
        if testColor[i] == sideToMove and testPiece[i] == KING:
            kingSquare = i
            break

    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] + i * 10]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == ROOK or testPiece[square] == QUEEN:
                return False
            else:
                break

    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] - i * 10]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == ROOK or testPiece[square] == QUEEN:
                return False
            else:
                break

    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] - i]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == ROOK or testPiece[square] == QUEEN:
                return False
            else:
                break

    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] + i]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == ROOK or testPiece[square] == QUEEN:
                return False
            else:
                break

    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] + i * 11]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == BISHOP or testPiece[square] == QUEEN:
                return False
            else:
                break
        
    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] + i * 9]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == BISHOP or testPiece[square] == QUEEN:
                return False
            else:
                break

    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] - i * 9]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == BISHOP or testPiece[square] == QUEEN:
                return False
            else:
                break

    for i in range(1, 8):
        square = mailbox[mailbox64[kingSquare] - i * 11]
        if square == -1:
            break
        elif testColor[square] == sideToMove:
            break
        elif testColor[square] == xSideToMove:
            if testPiece[square] == BISHOP or testPiece[square] == QUEEN:
                return False
            else:
                break

    return True

def moveGeneration(color, piece, sideToMove, xSideToMove):
    potentialMoves = []
    for i in range(64):
        if color[i] == sideToMove:
            if piece[i] == PAWN:
                potentialMoves += pawnMoveGeneration(color, i, xSideToMove)
            elif piece[i] == KNIGHT:
                potentialMoves += knightMoveGeneration(color, i, sideToMove)
            elif piece[i] == BISHOP:
                potentialMoves += bishopMoveGeneration(color, i, xSideToMove)
            elif piece[i] == ROOK:
                potentialMoves += rookMoveGeneration(color, i, xSideToMove)
            elif piece[i] == QUEEN:
                potentialMoves += queenMoveGeneration(color, i, xSideToMove)
            elif piece[i] == KING:
                potentialMoves += kingMoveGeneration(color, i, sideToMove)
            else:
                print("ERROR: Invalid piece")
                return None
    
    legalMoves = []
    for move in potentialMoves:
        if checkIfMoveIsLegal(color, piece, sideToMove, xSideToMove, move):
            legalMoves.append(move)
    return legalMoves
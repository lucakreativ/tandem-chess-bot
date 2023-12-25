from constantsChess import *
from boardOperation import generateBoard

def pawnMoveGeneration(color, i, xSideToMove, enPassantSquare = -2):
    moves = []
    if xSideToMove == BLACK:
        if mailbox[mailbox64[i] + 1] == enPassantSquare:
            moves.append((i, i + 9, -3))

        if mailbox[mailbox64[i] - 1] == enPassantSquare:
            moves.append((i, i + 7, -3))




        if color[i + 8] == EMPTY:
            moves.append((i, i + 8, -2))

            if i >= 8 and i <= 15 and color[i + 16] == EMPTY:
                moves.append((i, i + 16, i + 16))


        if mailbox[mailbox64[i] + 11] != -1 and color[i + 9] == xSideToMove:
            moves.append((i, i + 9, -2))
        if mailbox[mailbox64[i] + 9] != -1 and color[i + 7] == xSideToMove:
            moves.append((i, i + 7, 1))


    if xSideToMove == WHITE:
        if mailbox[mailbox64[i] + 1] == enPassantSquare:
            moves.append((i, i - 7, -4))
        
        if mailbox[mailbox64[i] - 1] == enPassantSquare:
            moves.append((i, i - 9, -4))





        if color[i - 8] == EMPTY:
            moves.append((i, i - 8, -2))

            if i >= 48 and i <= 55 and color[i - 16] == EMPTY:
                moves.append((i, i - 16, i + 16))

        if mailbox[mailbox64[i] - 11] != -1 and color[i - 9] == xSideToMove:
            moves.append((i, i - 9, -2))
        if mailbox[mailbox64[i] - 9] != -1 and color[i - 7] == xSideToMove:
            moves.append((i, i - 7, -2))

    return moves

def knightMoveGeneration(color, i, sideToMove):
    moves = []
    for offsetMove in offset[1]:
        square = mailbox[mailbox64[i] + offsetMove]
        if square != -1 and color[square] != sideToMove:
            moves.append((i, square, -2))

    return moves

def bishopMoveGeneration(color, i, xSideToMove):
    moves = []
    for offsetMove in offset[2]:
        for j in range(1, 8):
            square = mailbox[mailbox64[i] + offsetMove * j]
            if square == -1:
                break
            elif color[square] == EMPTY:
                moves.append((i, square, -2))
            elif color[square] == xSideToMove:
                moves.append((i, square, -2))
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
                moves.append((i, square, -2))
            elif color[square] == xSideToMove:
                moves.append((i, square, -2))
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
                moves.append((i, square, -2))
            elif color[square] == xSideToMove:
                moves.append((i, square, -2))
                break
            else:
                break

    return moves

def kingMoveGeneration(color, i, sideToMove):
    moves = []
    for offsetMove in offset[5]:
        square = mailbox[mailbox64[i] + offsetMove]
        if square != -1 and color[square] != sideToMove:
            moves.append((i, square, -2))

    return moves



def notCheckIfBoardInCheck(testColor, testPiece, sideToMove, xSideToMove):
    for i in range(64):
        if testColor[i] == sideToMove and testPiece[i] == KING:
            kingSquare = i
            break

    if sideToMove == WHITE:
        if mailbox[mailbox64[kingSquare] + 11] != -1 and testColor[kingSquare + 9] == xSideToMove and testPiece[kingSquare + 9] == PAWN:
            return False
        if mailbox[mailbox64[kingSquare] + 9] != -1 and testColor[kingSquare + 7] == xSideToMove and testPiece[kingSquare + 7] == PAWN:
            return False
        
    if sideToMove == BLACK:
        if mailbox[mailbox64[kingSquare] - 11] != -1 and testColor[kingSquare - 9] == xSideToMove and testPiece[kingSquare - 9] == PAWN:
            return False
        if mailbox[mailbox64[kingSquare] - 9] != -1 and testColor[kingSquare - 7] == xSideToMove and testPiece[kingSquare - 7] == PAWN:
            return False

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

    for i in offset[1]:
        square = mailbox[mailbox64[kingSquare] + i]
        if square != -1 and testColor[square] == xSideToMove and testPiece[square] == KNIGHT:
            return False

    return True

def checkIfMoveIsLegal(color, piece, sideToMove, xSideToMove, move):
    testColor, testPiece = generateBoard(color, piece, move)
    
    return notCheckIfBoardInCheck(testColor, testPiece, sideToMove, xSideToMove)

    

def moveGeneration(color, piece, sideToMove, xSideToMove, enPassantSquare = -2):
    potentialMoves = []
    for i in range(64):
        if color[i] == sideToMove:
            if piece[i] == PAWN:
                potentialMoves += pawnMoveGeneration(color, i, xSideToMove, enPassantSquare)
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
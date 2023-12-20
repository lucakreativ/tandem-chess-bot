from constantsChess import *
from fenToPosition import fenToPosition

showMoves = True

def getSquare(i):
    file = "abcdefgh"[i % 8]
    rank = str(8 - i // 8)

    return file + rank

def shallowCopy(color, piece):
    colorCopy = []
    pieceCopy = []
    for i in range(64):
        colorCopy.append(color[i])
        pieceCopy.append(piece[i])
    return colorCopy, pieceCopy

def generateBoard(boardAfterMoves, color, piece, i, j, enPassant = False):
    if showMoves:
        print(getSquare(i) + " -> " + getSquare(j))

    colorCopy, pieceCopy = shallowCopy(color, piece)
    colorCopy[j] = colorCopy[i]
    pieceCopy[j] = pieceCopy[i]
    colorCopy[i] = EMPTY
    pieceCopy[i] = EMPTY

    if enPassant:
        if colorCopy[j] == WHITE:
            colorCopy[j - 8] = EMPTY
            pieceCopy[j - 8] = EMPTY
        else:
            colorCopy[j + 8] = EMPTY
            pieceCopy[j + 8] = EMPTY
    
    boardAfterMoves.append((colorCopy, pieceCopy))

    return boardAfterMoves

def offsetMoveGeneration(color, piece, sideToMove, xSideToMove, enPassantCheck = False, enPassantFile = -1):
    boardAfterMoves = []
    for i in range(64):
        if color[i] == sideToMove:
            if piece[i] == PAWN:
                if sideToMove == WHITE:
                    if color[i - 8] == EMPTY:
                        boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i - 8)
                        print(color[i - 16])
                        if i <= 55 and color[i - 16] == EMPTY:
                            boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i - 16)
                    if i >= 7 and color[i - 7] == xSideToMove and mailbox[mailbox64[i] - 9] != -1:
                        boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i - 7)
                    if i >= 9 and color[i - 9] == xSideToMove and mailbox[mailbox64[i] - 11] != -1:
                        boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i - 9)

                    
                    if enPassantCheck and i >= 32 and i <= 39:
                        if piece[i - 1] == PAWN and color[i - 1] == xSideToMove and enPassantFile == (i % 8) - 1 and mailbox[mailbox64[i] - 11] != -1:
                            boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i - 9, True)
                        if piece[i + 1] == PAWN and color[i + 1] == xSideToMove and enPassantFile == (i % 8) + 1 and mailbox[mailbox64[i] - 9] != -1:
                            boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i - 7, True)
                else:
                    if color[i + 8] == EMPTY:
                        boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i + 8)
                        if i <= 15 and color[i + 16] == EMPTY:
                            boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i + 16)
                    if i <= 56 and color[i + 7] == xSideToMove and mailbox[mailbox64[i] + 9] != -1:
                        boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i + 7)
                    if i <= 54 and color[i + 9] == xSideToMove and mailbox[mailbox64[i] + 11] != -1:
                        boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i + 9)

                    if enPassantCheck and i >= 24 and i <= 31:
                        if piece[i - 1] == PAWN and color[i - 1] == xSideToMove and enPassantFile == (i % 8) - 1 and mailbox[mailbox64[i] + 7] != -1:
                            boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i + 7, True)
                        if piece[i + 1] == PAWN and color[i + 1] == xSideToMove and enPassantFile == (i % 8) + 1 and mailbox[mailbox64[i] + 9] != -1:
                            boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, i + 9, True)
            
            else:
                for j in range(offsets[piece[i]]):
                    while True:
                        n = mailbox[mailbox64[i] + offset[piece[i]][j]]
                        if n == -1:
                            break
                        if color[n] != EMPTY:
                            if color[n] == xSideToMove:
                                boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, n)
                                break
                            if color[n] == sideToMove:
                                break
                        boardAfterMoves = generateBoard(boardAfterMoves, color, piece, i, n)
                        if not slide[piece[i]]:
                            break

    return boardAfterMoves



def printBoard(color, piece):
    for i in range(64):
        character = ""
        if i % 8 == 0 and i != 0:
            print()

        if color[i] == EMPTY:
            print(".", end="")
        elif piece[i] == PAWN:
            character = "P"
        elif piece[i] == KNIGHT:
            character = "N"
        elif piece[i] == BISHOP:
            character = "B"
        elif piece[i] == ROOK:
            character = "R"
        elif piece[i] == QUEEN:
            character = "Q"
        elif piece[i] == KING:
            character = "K"

        if color[i] == WHITE:
            print(character, end="")
        else:
            print(character.lower(), end="")
    print()


def main():
    color, piece = fenToPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    printBoard(color, piece)

    moves = offsetMoveGeneration(color, piece, WHITE, BLACK)

    for i in moves:
        printBoard(i[0], i[1])
        print("..................")


if __name__ == "__main__":
    main()
from constantsChess import *
from fenToPosition import fenToPosition

def getSquare(i):
    file = "abcdefgh"[i % 8]
    rank = str(8 - i // 8)

    return file + rank

def getMove(i, j, enPassant = False):
    print(getSquare(i) + " -> " + getSquare(j))


def offsetMoveGeneration(color, piece, sideToMove, xSideToMove, enPassantCheck = False, enPassantFile = -1):
    for i in range(64):
        if color[i] == sideToMove:
            if piece[i] == PAWN:
                if sideToMove == WHITE:
                    #must check if i-7 is on the same side with mailbox
                    if i >= 8 and color[i - 8] == 0:
                        getMove(i, i - 8)
                        if i < 16 and color[i - 16] == 0:
                            getMove(i, i - 16)
                    if i >= 7 and color[i - 7] == xSideToMove:
                        getMove(i, i - 7)
                    if i >= 9 and color[i - 9] == xSideToMove:
                        getMove(i, i - 9)

                    
                    if enPassantCheck and i >= 32 and i <= 39:
                        if piece[i - 1] == PAWN and color[i - 1] == xSideToMove and enPassantFile == (i % 8) - 1:
                            getMove(i, i - 9, True)
                        if piece[i + 1] == PAWN and color[i + 1] == xSideToMove and enPassantFile == (i % 8) + 1:
                            getMove(i, i - 7, True)
                else:
                    if i <= 55 and color[i + 8] == 0:
                        getMove(i, i + 8)
                        if i > 47 and color[i + 16] == 0:
                            getMove(i, i + 16)
                    if i <= 56 and color[i + 7] == xSideToMove:
                        getMove(i, i + 7)
                    if i <= 54 and color[i + 9] == xSideToMove:
                        getMove(i, i + 9)
            
            else:
                for j in range(offsets[piece[i]]):
                    while True:
                        n = mailbox[mailbox64[i] + offset[piece[i]][j]]
                        if n == -1:
                            break
                        if color[n] != EMPTY:
                            if color[n] == xSideToMove:
                                getMove(i, n)
                                break
                            if color[n] == sideToMove:
                                break
                        getMove(i, n)
                        if not slide[piece[i]]:
                            break



def printBoard(color, piece):
    for i in range(64):
        character = ""
        if i % 8 == 0 and i != 0:
            print()

        if piece[i] == PAWN:
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
        else:
            print(".", end="")

        if color[i] == WHITE:
            print(character, end="")
        else:
            print(character.lower(), end="")
    print()


def main():
    color, piece = fenToPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    printBoard(color, piece)

    offsetMoveGeneration(color, piece, WHITE, BLACK)


if __name__ == "__main__":
    main()
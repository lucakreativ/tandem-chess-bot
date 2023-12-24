from constantsChess import *

def generateBoard(color, piece, move):
    copyColor = color.copy()
    copyPiece = piece.copy()

    copyColor[move[1]] = copyColor[move[0]]
    copyPiece[move[1]] = copyPiece[move[0]]
    copyColor[move[0]] = EMPTY
    copyPiece[move[0]] = -1

    if move[2] == -3:
        copyColor[move[1] - 8] = EMPTY
        copyPiece[move[1] - 8] = -1
    elif move[2] == -4:
        copyColor[move[1] + 8] = EMPTY
        copyPiece[move[1] + 8] = -1


    return copyColor, copyPiece

def printBoard(color, piece):
    for i in range(8):
        for j in range(8):
            square = 63 - (i * 8 + j)
            if color[square] == WHITE:
                if piece[square] == PAWN:
                    print("P", end = "")
                elif piece[square] == KNIGHT:
                    print("N", end = "")
                elif piece[square] == BISHOP:
                    print("B", end = "")
                elif piece[square] == ROOK:
                    print("R", end = "")
                elif piece[square] == QUEEN:
                    print("Q", end = "")
                elif piece[square] == KING:
                    print("K", end = "")
                else:
                    print(".", end = "")
            elif color[square] == BLACK:
                if piece[square] == PAWN:
                    print("p", end = "")
                elif piece[square] == KNIGHT:
                    print("n", end = "")
                elif piece[square] == BISHOP:
                    print("b", end = "")
                elif piece[square] == ROOK:
                    print("r", end = "")
                elif piece[square] == QUEEN:
                    print("q", end = "")
                elif piece[square] == KING:
                    print("k", end = "")
                else:
                    print(".", end = "")
            else:
                print(".", end = "")
        print()


def printMove(move):
    file = "abcdefgh"[7 - (move[0] % 8)]
    rank = move[0] // 8

    file2 = "abcdefgh"[7 - (move[1] % 8)]
    rank2 = move[1] // 8

    print(file + str(rank + 1) + " --> " + file2 + str(rank2 + 1))
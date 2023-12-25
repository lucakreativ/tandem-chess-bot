from fenToPosition import fenToPosition
from constantsChess import *
from moveGeneration import moveGeneration, generateBoard
from boardOperation import *
from evaluatePosition import evaluate
from search import negaMax, maxi, mini

def ueserMove(color, piece, move):
    rank1=8-int(move[1])
    file2=ord(move[0])-ord('a')
    i = 63 - (rank1 * 8 + file2)
    rank2=8-int(move[3])
    file2=ord(move[2])-ord('a')
    j = 63 - (rank2 * 8 + file2)

    enPassantSquare = -2
    if color[i] == WHITE:
        if piece[i] == PAWN and j - i == 16:
            enPassantSquare = j

    return (i, j, enPassantSquare)

def main():
    color, piece = fenToPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    while True:
        printBoard(color, piece)
        move = input("Enter move: ")
        move = ueserMove(color, piece, move)
        
        color2, piece2 = generateBoard(color, piece, move)
        printBoard(color2, piece2)
        eval, moves, machineMove = mini(color2, piece2, BLACK, WHITE, None, 1)
        print("\n", eval, moves)
        color, piece = generateBoard(color2, piece2, machineMove)


if __name__ == "__main__":
    main()
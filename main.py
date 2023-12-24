from fenToPosition import fenToPosition
from constantsChess import *
from moveGeneration import moveGeneration, generateBoard

def main():
    color, piece = fenToPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    moves = moveGeneration(color, piece, WHITE, BLACK)
    for move in moves:
        color2, piece2 = generateBoard(color, piece, move)
        moves2 = moveGeneration(color2, piece2, BLACK, WHITE)
        print(len(moves2))

if __name__ == "__main__":
    main()
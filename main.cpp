#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <cctype>
#include <string>

#include "fenToPosition.hpp"
//#include "constants.hpp"


using namespace std;

string getSquare(int i) {
    string file;
    switch (i%8) {
        case 0:
            file = 'a';
            break;
        case 1:
            file = 'b';
            break;
        case 2:
            file = 'c';
            break;
        case 3:
            file = 'd';
            break;
        case 4:
            file = 'e';
            break;
        case 5:
            file = 'f';
            break;
        case 6:
            file = 'g';
            break;
        case 7:
            file = 'h';
            break;
        default:
            file = "error";
            break;
    }

    int row = i/8+1;
    
    return file + to_string(row);
}

void getMove(int i, int j) {
    cout << getSquare(i) << " -> " << getSquare(j) << endl;
}

vector<int[]> offsetMoveGeneration(int color[64], int piece[64], int sideToMove, int notSideToMove) {
    vector<int[]> moveList;
    for (int i = 0; i < 64; i++) {
        if (color[i] == sideToMove) {
            int prePiece = piece[i];
            if (prePiece != PAWN) {
                for (int j = 0; j < offsets[prePiece]; j++) {
                    for (int n = i;;) {
                        n = mailbox[mailbox64[n] + offset[prePiece][j]];
                        if (n == -1) break;
                        if (color[n] != EMPTY) {
                            if (color[n] == notSideToMove) {
                                cout << "Capture move" << "\n";
                                moveList.push_back({i, n});
                                break;
                            }
                            if (color[n] == sideToMove) break;
                        }
                        cout << "Quiet move" << "\n";
                        moveList.push_back({i, n});
                        if (!slide[prePiece]) break;
                    }
                }
            } else {
                if (color[i]==WHITE){
                    if (color[i-8]==EMPTY) {
                        cout << "Pawn move" << "\n";
                        moveList.push_back({i, i-8});
                        if (48<=i && i<=55 && sideToMove == WHITE && mailbox[mailbox64[i]-20]!=-1 && color[i-16]==EMPTY) {
                            cout << "Douple pawn move" << "\n";
                            moveList.push_back({i, i-16});
                        }
                    }
                    if (mailbox[mailbox64[i]-9]!=-1 && color[i-7]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        moveList.push_back({i, i-7});
                    }
                    if (mailbox[mailbox64[i]-11]!=-1 && color[i-9]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        moveList.push_back({i, i-9});
                    }
                }
                if (color[i]==BLACK){
                    if (color[i+8]==EMPTY) {
                        cout << "Pawn move" << "\n";
                        moveList.push_back({i, i+8});
                        if (8<=i && i<=15 && sideToMove == BLACK && mailbox[mailbox64[i]+20]!=-1 && color[i+16]==EMPTY) {
                            cout << "Douple pawn move" << "\n";
                            moveList.push_back({i, i+16});
                        }
                    }
                    if (mailbox[mailbox64[i]+9]!=-1 && color[i+7]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        moveList.push_back({i, i+7});
                    }
                    if (mailbox[mailbox64[i]+11]!=-1 && color[i+9]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        moveList.push_back({i, i+9});
                    }
                }
            }
        }
    }

    return moveList;
}



void printBoard(int color[64], int piece[64]) {
    for (int i = 0; i < 64; i++) {
        if (i != 0 && i % 8 == 0) {
            cout << "\n";
        }


        if (color[i] != EMPTY) {
            char toPrint;
            switch (piece[i]) {
                case 0:
                    toPrint = 'p';
                    break;
                case 1:
                    toPrint = 'n';
                    break;
                case 2:
                    toPrint = 'b';
                    break;
                case 3:
                    toPrint = 'r';
                    break;
                case 4:
                    toPrint = 'q';
                    break;
                case 5:
                    toPrint = 'k';
                    break;
                default:
                    break;
            }

            if (color[i] == 1) {
                toPrint = toupper(toPrint);
            }

            cout << toPrint;
        } else {
            cout << " ";
        } 
    }
    cout << "\n";
}



void printColor(int color[64], int piece[64]) {
    for (int i = 0; i < 64; i++) {
        if (i != 0 && i % 8 == 0) {
            cout << "\n";
        }


        cout << color[i];
    }
    cout << "\n";
}



int main() {
    int color[64];
    int piece[64];

    vector<vector<int>> dataFenToPosition;

    dataFenToPosition = fenToPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    copy(dataFenToPosition.at(0).begin(), dataFenToPosition.at(0).end(), color);
    copy(dataFenToPosition.at(1).begin(), dataFenToPosition.at(1).end(), piece);

    printColor(color, piece);
    offsetMoveGeneration(color, piece, WHITE, BLACK);


    return 0;
}
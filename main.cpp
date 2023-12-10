#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <cctype>

#include "fenToPosition.hpp"
//#include "constants.hpp"


using namespace std;

void offsetMoveGeneration(int color[64], int piece[64], int sideToMove, int notSideToMove) {
    int counter = 0;
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
                                counter++;
                                break;
                            }
                            
                        }
                        cout << "Quiet move" << "\n";
                        counter++;
                        if (!slide[prePiece]) break;
                    }
                }
            } else {
                if (color[i]==WHITE){
                    if (color[i-8]==EMPTY) {
                        cout << "Pawn move" << "\n";
                        counter++;
                        if (56<=i && i<=63 && sideToMove == WHITE && mailbox[mailbox64[i]-20]!=-1 && color[i-16]==EMPTY) {
                            cout << "Douple pawn move" << "\n";
                            counter++;
                        }
                    }
                    if (mailbox[mailbox64[i]-9]!=-1 && color[i-7]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        counter++;
                    }
                    if (mailbox[mailbox64[i]-11]!=-1 && color[i-9]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        counter++;
                    }
                }
                if (color[i]==BLACK){
                    if (color[i+8]==EMPTY) {
                        cout << "Pawn move" << "\n";
                        counter++;
                        if (8<=i && i<=15 && sideToMove == BLACK && mailbox[mailbox64[i]+20]!=-1 && color[i+16]==EMPTY) {
                            cout << "Douple pawn move" << "\n";
                            counter++;
                        }
                    }
                    if (mailbox[mailbox64[i]+9]!=-1 && color[i+7]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        counter++;
                    }
                    if (mailbox[mailbox64[i]+11]!=-1 && color[i+9]==notSideToMove) {
                        cout << "Pawn capture" << "\n";
                        counter++;
                    }
                }
            }
        }
    }
    cout << counter << endl;
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

int main() {
    int color[64];
    int piece[64];

    vector<vector<int>> dataFenToPosition;

    dataFenToPosition = fenToPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    copy(dataFenToPosition.at(0).begin(), dataFenToPosition.at(0).end(), color);
    copy(dataFenToPosition.at(1).begin(), dataFenToPosition.at(1).end(), piece);

    //printBoard(color, piece);
    offsetMoveGeneration(color, piece, WHITE, BLACK);


    return 0;
}
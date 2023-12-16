#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <cctype>

#include "constants.hpp"

using namespace std;

vector<vector<int>> fenToPosition(string fen) {
    int color[64];
    int piece[64];

    bool reachedEndOfPosition = false;
    int counter = 0;
    for (int i = 0; i < fen.length() && !reachedEndOfPosition; i++) { 
        char charAtIndex = fen[i];
        if (charAtIndex == ' '){
            reachedEndOfPosition = true;
        } else if (charAtIndex != '/') {
            if (islower(charAtIndex)) {
                color[counter] = BLACK;
            } else if (isupper(charAtIndex)) {
                color[counter] = WHITE;
            } else if (!isdigit(charAtIndex)) {
                cout << "Error: cant decode " << charAtIndex << "\n";
            }

            char lowercaseCharAtIndex = tolower(charAtIndex);

            switch (lowercaseCharAtIndex) {
            case 'p':
                piece[counter] = PAWN;
                break;
            case 'n':
                piece[counter] = KNIGHT;
                break;
            case 'b':
                piece[counter] = BISHOP;
                break;
            case 'r':
                piece[counter] = ROOK;
                break;
            case 'q':
                piece[counter] = QUEEN;
                break;
            case 'k':
                piece[counter] = KING;
                break;
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
                for (int j = 0; j <= (charAtIndex - '0') - 1; j++) {
                    color[counter + j] = EMPTY;
                }
                counter += (charAtIndex - '0') - 1;
                break;

            default:
                cout << "Error: piece or empty square couldn't be decoded " << lowercaseCharAtIndex << "\n";
                break;
            }

            if (counter >= 64) {
                cout << "Error: too many pieces on the board " << i << "\n";
            } else {
                counter ++;
            }
        }
    } 

    vector<int> vectorColor(color, color + sizeof color / sizeof color[0]);
    vector<int> vectorPiece(piece, piece + sizeof piece / sizeof piece[0]);
    vector<vector<int>> returningArrays = {vectorColor, vectorPiece};
    return returningArrays;
}
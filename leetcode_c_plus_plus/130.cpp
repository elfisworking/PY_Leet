// 130. 被围绕的区域
// https://leetcode-cn.com/problems/surrounded-regions/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 130.cpp
@Time : 2022/03/31 16:39:16
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
private:
    int board_row;
    int board_col;
public:
    void solve(vector<vector<char>>& board) {
        int row = board.size(), col = board[0].size();
        board_row = row;
        board_col = col;
        for(int i = 0; i < col; i++) {
            if(board[0][i] == 'O') {
                dfs(board, 0, i);
            }
            if(board[row - 1][0] == 'O') {
                dfs(board, row - 1, i);
            }
        }
        for(int i = 0; i < row; i++) {
            if(board[i][0] == 'O') {
                dfs(board, i, 0);
            }
            if(board[i][col - 1] == 'O') {
                dfs(board, i, col - 1);
            }
        }
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++) {
                if(board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if(board[i][j] == '1') {
                    board[i][j] = 'O';
                }
            }
        }

    }

    void dfs(vector<vector<char>>& board, int row, int col) {
        if(board[row][col] == 'O') {
            board[row][col] = '1';
        } else {
            return;
        }
        int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for(int i = 0; i < 4; i++) {
            int new_row = dir[i][0] + row;
            int new_col = dir[i][1] + col;
            if(new_row < 0 || new_row >= board_row || new_col < 0 || new_col >= board_col) continue;
            dfs(board, new_row, new_col);
        }
        

    }
};
using namespace std;
#include<vector>
class NumMatrix {
public:
    // 傻逼代码 跟官方一样结果超时
    vector<vector<int>> sums ;
    NumMatrix(vector<vector<int>>& matrix) {
        int row = matrix.size();
        if(row > 0){
            int col = matrix[0].size();
            sums.resize(row+1,vector<int>(col+1));
            for(int i = 1;i < row+1;i++){
                for(int j = 1;j < col+1;j++){
                    sums[i][j] = sums[i-1][j]+sums[i][j-1]+matrix[i-1][j-1]-sums[i-1][j-1];
                }
            }
        }
        
    }

    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return sums[row2 + 1][col2 + 1] - sums[row1][col2 + 1] - sums[row2 + 1][col1] + sums[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
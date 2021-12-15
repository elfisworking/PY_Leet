// 剑指 Offer 13. 机器人的运动范围
// https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer13.cpp
@Time : 2021/12/13 20:02:25
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
private:
    int rows;
    int cols;
public:
    int movingCount(int m, int n, int k) {
        rows = m;
        cols = n;
        vector<vector<bool>> visted(m, vector<bool>(n, false));
        return walk(0, 0, k, visted);
        
    }

    int walk(int x, int y, int k, vector<vector<bool>> & visted) {
        if(x < 0 || x >= rows || y < 0 || y >= cols || visted[x][y]) return 0;
        if(number(x) + number(y) > k) return 0;
        visted[x][y] = true;
        return walk(x, y + 1, k, visted) + walk(x, y - 1, k, visted) + walk(x + 1, y, k, visted) + walk(x - 1, y, k, visted) + 1;

    }

    int number(int x){
        int num = 0;
        while(x) {
            num += x % 10;
            x /= 10;
        }
        return num;
    }
};

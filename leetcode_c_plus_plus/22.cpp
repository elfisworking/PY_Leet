// 22. 括号生成
// https://leetcode-cn.com/problems/generate-parentheses/
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
@File : 22.cpp
@Time : 2022/01/19 22:27:37
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if(n < 1) return vector<string>{};
        vector<string> ans;
        int left = n, right = n;
        string path = "";
        dfs(ans, left, right, path);
        return ans;

    }

    void dfs(vector<string>& ans,int left, int right, string& path) {
        if(left == 0 && right == 0) {
            ans.push_back(path);
            return;
        }
        if(left > 0) {
            path.push_back('(');
            dfs(ans, left - 1, right, path);
            path.pop_back();
        }
        if(left < right) {
            path.push_back(')');
            dfs(ans, left, right - 1, path);
            path.pop_back();
        }
    }
};
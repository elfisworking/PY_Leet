// 46. 全排列
// https://leetcode-cn.com/problems/permutations/
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
@File : 46.cpp
@Time : 2021/12/30 19:30:12
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
**/
class Solution {
public:

    void dfs(vector<int>& nums, vector<bool>& visited, vector<int>& path, vector<vector<int>>&ans) {
        if(path.size() == nums.size()) {
            return ans.push_back(path);
        }
        for(int i = 0; i < nums.size(); i++) {
            if(visited[i]) continue;
            visited[i] = true;
            path.push_back(nums[i]);
            dfs(nums, visited, path, ans);
            path.pop_back();
            visited[i] = false;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int size = nums.size();
        vector<bool> visited(size, false);
        vector<vector<int>> ans;
        vector<int> path;
        dfs(nums, visited, path, ans);
        return ans;

    }
};

class Solution {
public:
    void backtrack(vector<vector<int>>& res, vector<int>& output, int first, int len){
        // 所有数都填完了
        if (first == len) {
            res.emplace_back(output);
            return;
        }
        for (int i = first; i < len; ++i) {
            // 动态维护数组
            swap(output[i], output[first]);
            // 继续递归填下一个数
            backtrack(res, output, first + 1, len);
            // 撤销操作
            swap(output[i], output[first]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> > res;
        backtrack(res, nums, 0, (int)nums.size());
        return res;
    }
};

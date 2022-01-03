// 面试题 16.20. T9键盘
// https://leetcode-cn.com/problems/t9-lcci/
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
@File : 16.20.cpp
@Time : 2022/01/03 21:34:47
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Medium
**/

class Solution {
private:
    // 这里数字是2从开始，2对应的编号是0
    // 一共26个字母，对应a-z
    int char2num[26] = {0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7};

    bool IsMatch(int* nums, const string& word, int n)
    {
        // word里字母按照从0来换算是否和数字里匹配
        for (int i = 0; i < n; ++i)
        {
            if (char2num[word[i]-'a'] != nums[i])
            {
                return false;
            }
        }
        return true;
    }
public:
    vector<string> getValidT9Words(string num, vector<string>& words) {
        // 把num从string转换为数字，这里要减去2
        int n = num.size();
        int *nums = new int[n];
        for (int i = 0; i < n; ++i)
        {
            nums[i] = num[i] - '2';
        }

        vector<string> res;
        for (const string& word : words)
        {
            if (IsMatch(nums, word, n)) res.push_back(word);
        }
        return res;
    }
};
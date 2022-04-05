// 140. 单词拆分 II
// https://leetcode-cn.com/problems/word-break-ii/
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
@File : 140.cpp
@Time : 2022/03/26 16:14:25
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_map<string, vector<string>> map;
        return helper(map, wordDict, s);
    }
    
    vector<string> helper(unordered_map<string, vector<string>>& m, vector<string>& wordDict, string s) {
        if(m.count(s)) return m[s];
        if(s.empty()) return {""};
        vector<string> res;
        for(auto word : wordDict) {
            if(s.substr(0, word.size()) != word) continue;

            vector<string> tmp = helper(m, wordDict, s.substr(word.size()));
            for(auto itm : tmp) {
                res.push_back(word + (itm.empty() ? "" : " " + itm));
            }
        }
        m[s] = res;
        return res;

    }


};
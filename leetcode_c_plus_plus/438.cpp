// 438. 找到字符串中所有字母异位词
// https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : 438.cpp
@Time : 2021/11/28 20:59:54
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int sLen = s.size();
        int pLen = p.size();
        vector<int> ans;
        int count[26] = {0};
        if(pLen > sLen) return ans;
        
        for(int j = 0; j < pLen; j++){
            count[p[j] - 'a']++;
            count[s[j] - 'a']--;
        }
        int differ = 0;
        for(int i = 0; i < 26; i++){
            if(count[i] != 0) differ++;
        }
        if(differ == 0) ans.push_back(0);
        for(int i = 0; i < sLen - pLen; i++){
            if(count[s[i] - 'a'] == -1) differ--;
            else if(count[s[i] - 'a'] == 0) differ++;
            count[s[i] - 'a']++;
            if(count[s[i + pLen] - 'a'] == 1) differ--;
            else if(count[s[i + pLen] - 'a'] == 0) differ++;
            count[s[i + pLen] - 'a']--;
            if(differ == 0) ans.push_back(i + 1); 
        }
        return ans;

    }
};
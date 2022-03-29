// 744. 寻找比目标字母大的最小字母
// https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/
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
@File : 744.cpp
@Time : 2022/03/25 15:13:59
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0, right = letters.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(letters[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        if(left == letters.size()) {
            return letters[0];
        }
        return letters[left];

    }
};
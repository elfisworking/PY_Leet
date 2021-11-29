// 剑指 Offer 53 - I. 在排序数组中查找数字 I
// https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer53I.cpp
@Time : 2021/11/29 16:02:37
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    int search(vector<int>& nums, int target) {
            unordered_map<int, int> map;
            for(int i :nums) {
                if(map.count(i)) map[i]++;
                else map[i] = 1;
            }
            if(!map.count(target)) return 0;
            return map[target];
    }
};
// 剑指 Offer 39. 数组中出现次数超过一半的数字
// https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
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
@File : offer39.cpp
@Time : 2021/12/18 14:13:41
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking : 摩尔投票
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int num = 0;
        int count = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(count == 0) {
                num = nums[i];
            }
            if(num == nums[i]) {
                count++;
            }else{
                count--;
            }
        }
        return num;

    }
};
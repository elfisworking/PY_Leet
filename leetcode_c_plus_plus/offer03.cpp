// 剑指 Offer 03. 数组中重复的数字
// https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer03.cpp
@Time : 2021/11/29 16:10:35
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        unordered_map<int, int> map;
        for(auto i : nums) {
            if(map.count(i)) return i;
            map[i] = 1;
        }
        return 0;

    }
};


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = this->binarySearchLeft(nums, target);
        int right = this->binarySearchRight(nums, target);
        cout << left << right << endl;
        int ans = 0;
        for(int i =left; i < right ; i++) 
            ans++;
        return ans;
    }
    int binarySearchLeft(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] >= target) right = mid;
            else left = mid + 1;
        }
        return left;
    }
    int binarySearchRight(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] > target) right = mid;
            else left = mid + 1;
        }
        return left;
    }
};
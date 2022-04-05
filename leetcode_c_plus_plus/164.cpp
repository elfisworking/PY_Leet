// 164. 最大间距
// https://leetcode-cn.com/problems/maximum-gap/
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
@File : 164.cpp
@Time : 2022/03/31 23:24:56
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    // O(n)
    int maximumGap(vector<int>& nums) {
        int size = nums.size();
        if(size < 2) return 0;
        int minVal = *min_element(nums.begin(), nums.end());
        int maxVal = *max_element(nums.begin(), nums.end());
        int d = max(1, (maxVal - minVal) / (size - 1));
        int bucketSize = (maxVal - minVal) /d + 1;
        vector<pair<int, int>> bucket(bucketSize, {-1, -1});
        for(int i = 0; i < size; i++) {
            int idx = (nums[i] - minVal) / d;
            if(bucket[idx].first == -1) {
                bucket[idx].first = bucket[idx].second = nums[i];
            } else {
                bucket[idx].first = min(bucket[idx].first, nums[i]);
                bucket[idx].second = max(bucket[idx].second, nums[i]);
            }
        }
        int ret = 0;
        int prev = -1;
        for(int i = 0; i < bucketSize; i++) {
            if(bucket[i].first == -1) continue;
            if(prev != -1) {
                ret = max(ret, bucket[i].first - bucket[prev].second);
            }
            prev = i;
        }
        return ret;

    }
};
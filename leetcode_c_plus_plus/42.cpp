// 42. 接雨水
// https://leetcode-cn.com/problems/trapping-rain-water/
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
@File : 42.cpp
@Time : 2022/04/07 20:32:39
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        int l = height.size();
        int left = 0;
        int right = 0;
        int h = 1;
        int max_val = 0;
        for(auto x : height) {
            max_val = max(max_val, x);
        }
        while(h <= max_val) {
            for(int i = 0; i < l; i++) {
                if(height[i] >= h) {
                    left = i;
                    break;
                }
            }
            right = left + 1;
            while(right < l) {
                if(height[right] >= h) {
                    ans += (right - left - 1);
                    left = right;
                }
                right++;
            }
            h++;
        }
        return ans;
    }
};

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) {
            return 0;
        }
        vector<int> leftMax(n);
        leftMax[0] = height[0];
        for (int i = 1; i < n; ++i) {
            leftMax[i] = max(leftMax[i - 1], height[i]);
        }

        vector<int> rightMax(n);
        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            rightMax[i] = max(rightMax[i + 1], height[i]);
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += min(leftMax[i], rightMax[i]) - height[i];
        }
        return ans;
    }
};
// LCP 18. 早餐组合
// https://leetcode-cn.com/problems/2vYnGI/
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
@File : lcp18.cpp
@Time : 2022/04/04 20:28:54
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    int breakfastNumber(vector<int>& staple, vector<int>& drinks, int x) {
        sort(staple.begin(), staple.end());
        sort(drinks.begin(), drinks.end());
        int prev = 0;
        int ans = 0;
        for(int i = 0; i < staple.size(); i++) {
            if(i > 0 && staple[i] == staple[i - 1]) {
                ans += prev;
                continue;
            }
            int num = bisect(drinks, staple[i], x);
            if(num == 0) break;
            ans = (ans + num) %  1000000007;
            prev = num;
        }
        return ans;
    }

    int bisect(vector<int>& drinks, int val, int x) {
        int left = 0, right = drinks.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(drinks[mid] + val > x) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return right;

    }
};
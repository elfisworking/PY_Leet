// 11. 盛最多水的容器
// https://leetcode-cn.com/problems/container-with-most-water/
using namespace std;
#include<vector>
class Solution {
public:
    int getMax(int val1,int val2){
        if(val1>=val2)
            return val1;
        return val2;
    }
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int max_val = 0;
        while(left<right){
            if(height[left]<=height[right]){
                max_val = getMax(max_val,height[left]*(right-left));
                left++;
            }else{
                max_val = getMax(max_val,height[right]*(right-left));
                right--;
            }
        }
        return max_val;
    }
};
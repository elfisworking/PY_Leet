// 15. 三数之和
// https://leetcode-cn.com/problems/3sum/
using namespace std;
#include<vector>
#include<algorithm>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int length = nums.size();
        vector<vector<int>> ans;
        if(length<3){
            return ans;
        }
        sort(nums.begin(),nums.end());
        int left = 0;
        int right ;
        int middle;
        while(left<right-1){
            if(nums[left]>0)
                break;
            if(left > 0 && nums[left-1] == nums[left]){
                left++;
                continue;
            }
            middle = left+1;
            right = length-1; 
            while(middle<right){
                if(middle>left+1 && nums[middle-1]==nums[middle]){
                    middle++;
                    continue;
                }
                int val = nums[left]+nums[middle]+nums[right];
                if(val == 0){
                    ans.push_back(vector<int>{nums[left],nums[middle],nums[right]});
                    //break; 不能直接break 可能会漏掉答案
                    middle++;
                }else if (val < 0)
                {
                    middle++;
                }else
                {
                    right--;
                }           
            }
            left++;
            
        }
        return ans;

    }
};
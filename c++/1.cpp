// 1. 两数之和
// https://leetcode-cn.com/problems/two-sum/
using namespace std;
#include<vector>
#include<unordered_map>
class Solution {
public:
    // 哈希表
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m ;
        vector<int> ans;
        for(int i=0 ; i<nums.size();i++){
            int minus = target-nums[i];
            if(m.count(minus)){
                ans.push_back(m[minus]);
                ans.push_back(i);
                return ans;
            }else{
                m[nums[i]] = i;
            }
        }
        return ans;

    }
};
// 27. 移除元素
// https://leetcode-cn.com/problems/remove-element/
using namespace std;
#include <vector>
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int length = nums.size();
        if (length == 0) return 0;
        int left = -1;
        int right = 0;
        while(right < length){
            if(nums[right] != val){
                left++;
                nums[left] = nums[right];
            }
            right++;
        }
        return left+1;
    }
};
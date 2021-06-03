// 26. 删除有序数组中的重复项
// https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
using namespace std;
#include <vector>
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length  = nums.size();
        if(length == 0){
            return 0;
        }
        int left = 0;
        int right = 0;
        while(right < length){
            if( right>0 &&  nums[left] != nums[right]){
                left++;
                nums[left] = nums[right];
            }
            right++;
        }
        return left+1;
    }
};
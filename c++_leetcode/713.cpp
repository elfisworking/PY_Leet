using namespace std;
#include <vector>
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int left = 0 , right = 0;
        int mul = 1;
        int ans = 0;
        while(right < nums.size()){
            mul *= nums[right];
            while(mul >= k && left <= right ){
                mul /= nums[left];
                left++;
            }
            ans += right - left + 1;
            right++;
        }
        return ans;
    }
};
#include<vector>
#include<numeric>
using namespace std;
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int a  = (nums.size() + 1) * nums.size() / 2;
        int b  = 0;
        b = accumulate(nums.begin(), nums.end(), b);
        return a - b;
    }
};
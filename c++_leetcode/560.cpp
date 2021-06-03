using namespace std;
#include <iostream>
#include <vector>
#include <unordered_map>
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int size = nums.size();
        int prefix[size+1];
        prefix[0] = 0;
        int i = 1;
        for(auto val : nums){
            cout<<val<<endl;
            prefix[i] = prefix[i-1]+val;
            i++;
        }
        int res = 0;
        unordered_map<int,int> m;
        m[0] = 1;
        for(int i= 1;i<size+1;i++){
            int j = prefix[i]-k;
            if(m[j]){
                res += m[j];
            }
            m[prefix[i]]++;
        }
        return res;

    }
};
int main(){
    Solution s ;
    vector<int>nums{1,1,1};
    int res = s.subarraySum(nums,2);
    cout<<res<<endl;
    return 0;
}
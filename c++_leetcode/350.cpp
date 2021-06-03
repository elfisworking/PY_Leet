// 350. 两个数组的交集 II
// https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
using namespace std;
#include <vector>
#include <unordered_map>
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        unordered_map<int,int> m;
        for(auto i : nums1){
            m[i]++;
        }
        for(int a : nums2){
            if(m.count(a)){
                ans.push_back(a);
                m[a]--;
                if(m[a] == 0){
                    m.erase(a);
                }
            }
        }
        return ans;
    }
};
using namespace std;
#include <vector>
#include <unordered_set>
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s1(nums1.begin(),nums1.end());
        unordered_set<int> s2(nums2.begin(),nums2.end());
        vector<int> res;
        for(auto itr = s2.begin();itr != s2.end();itr++){
            if (s1.count(*itr)){
                res.push_back(*itr);
            }
        }
        return res;
    }
};
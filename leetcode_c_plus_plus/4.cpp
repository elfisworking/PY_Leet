#include<unordered_map>
#include<cmath>
#include<string>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        unordered_map<char, int> map;
        int start =0 , end = 0;
        int length = s.size();
        while(end < length) {
            int num = map.count(s[end]);
            if(num > 0) {
                start = max(map[s[end]], start);
            }
            map[s[end]] = end + 1;

            ans = max(end - start + 1, ans);
            end++;
        }
        return ans;        

    }
};
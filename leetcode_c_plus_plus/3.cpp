#include <iostream>
#include <map>
#include <string>
#include <cmath>
#include <set>
using namespace std;
int lengthOfLongesSubstring(string s);//function prototype
int lengthOfLongesSubstringForce(string s);

int main() {
    string s = "pwwkew";
    int ans = lengthOfLongesSubstring(s);
    cout << ans << endl;
    return 0;
}

int lengthOfLongestSubstring(string s) {
    int ans = 0;
    int length = s.length();
    map<char,int> charMap;
    int end = 0;
    int start = 0;
    while( end < length) {
        char ch = s[end];
        auto iter = charMap.find(ch);
        if(iter != charMap.end()) {
            start = max(charMap[ch], start);
        }
        ans = max(ans, end - start + 1);
        charMap[ch] = end + 1;
        end++;
    }
    return ans;
}

int lengthOfLongesSubstring(string s) {
    int ans = 0;
    for(int i = 0; i < s.length(); i ++) {
        int currMax = 1;
        set<char> charSet;
        for(int j = i; j < s.length(); j++) {
            int num = charSet.count(s[j]);
            if(num == 0) {
                currMax = max(currMax, j - i + 1);
                charSet.insert(s[j]);
            } else {
                break;
            }

        }
        ans = max(ans, currMax);
    }
    return ans;
}

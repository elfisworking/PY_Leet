//
// https://leetcode-cn.com/problems/simplify-path/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 71.cpp
@Time : 2022/01/06 23:03:48
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag :Medium
**/
class Solution {
public:
    string simplifyPath(string path) { 
        vector<string> v;
        string s = "";
        for(int i = 0; i < path.size(); i++) {
            if(path[i] == '/') {
                if(s.size() > 0) {
                    v.push_back(s);
                    s = "";
                }                
            } else {
                s.push_back(path[i]);
            }
        }
        if(s.size() > 0) v.push_back(s);
        stack<string> st;
        for(int i = 0; i < v.size(); i++) {
            if(v[i] == ".") continue;
            else if(v[i] == "..") {
                if(!st.empty()) st.pop();
            }
            else st.push(v[i]);
        }
        string ans = "";
        while(!st.empty()) {
            string tmp = st.top();
            ans =  "/" + tmp + ans;
            st.pop();
        }
        if(ans.size() == 0) ans = "/";
        return ans;

    }
};
// 310. 最小高度树
// https://leetcode-cn.com/problems/minimum-height-trees/
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
@File : 310.cpp
@Time : 2022/04/06 19:56:52
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n == 1) {
            return {0};
        }
        vector<int> degree(n);
        vector<vector<int>> adj(n);
        for(auto & edge : edges) {
            adj[edge[0]].emplace_back(edge[1]);
            adj[edge[1]].emplace_back(edge[0]);
            degree[edge[0]]++;
            degree[edge[1]]++;
        }
        queue<int> q;
        vector<int> ans;
        for(int i = 0; i < n; i++) {
            if(degree[i] == 1) {
                q.emplace(i);
            }
        }
        int remainNodes = n;
        while(remainNodes > 2) {
            int sz = q.size();
            remainNodes -= sz;
            for(int i = 0; i < sz; i++) {
                int curr = q.front();
                q.pop();
                for(auto & v : adj[curr]) {
                    if(--degree[v] == 1) {
                        q.emplace(v);
                    }
                }
            }
        }
        while(!q.empty()) {
            ans.emplace_back(q.front());
            q.pop();
        }
        return ans;



    }

};
//
//
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
@File : 3.cpp
@Time : 2022/04/18 21:18:13
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/

class Solution {
public:
    vector<int> lightSticks(int height, int width, vector<int>& indices) {
        int n = (height + 1) * (width + 1), m = (height + 1) * width + height * (width + 1);
        vector<vector<int>> adj(n);
        vector<bool> bad(m);
        for (int idx : indices)
            bad[idx] = true;
        for (int i = 0; i <= height; ++i)
            for (int j = 0; j <= width; ++j) {
                int idx = i * (width + 1) + j;
                if (i + 1 <= height) {
                    int nxt = (i + 1) * (width + 1) + j;
                    int edge = (i + 1) * width + i * (width + 1) + j;
                    if (!bad[edge]) {
                        adj[idx].push_back(nxt);
                        adj[nxt].push_back(idx);
                    }
                }
                
                if (j + 1 <= width) {
                    int nxt = i * (width + 1) + j + 1;
                    int edge = i * width + i * (width + 1) + j;
                    if (!bad[edge]) {
                        adj[idx].push_back(nxt);
                        adj[nxt].push_back(idx);
                    }
                }
            }
        
        int cnt = 0;
        
        for (int i = 0; i < n; ++i)
            if (!adj[i].empty())
                cnt++;
        
        int best = INT_MAX;
        vector<int> ans;
        for (int i = 0; i < n; ++i) {
            queue<pair<int, int>> q;
            q.emplace(i, 0);
            int rem = cnt - 1;
            vector<bool> vis(n);
            vis[i] = true;
            int hi = 0;
            
            while (!q.empty()) {
                auto [u, t] = q.front();
                q.pop();
                hi = t;
                for (int v : adj[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        rem--;
                        q.emplace(v, t + 1);
                    }
                }
            }
            
            if (rem != 0)
                continue;
            
            if (hi < best) {
                ans.clear();
                best = hi;
            }
            
            if (hi == best)
                ans.push_back(i);
        }
        
        return ans;
    }
};



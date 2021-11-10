// 543. 二叉树的直径
// https://leetcode-cn.com/problems/diameter-of-binary-tree/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
/**
@File : 543.cpp
@Time : 2021/11/09 23:15:09
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans;
    int diameterOfBinaryTree(TreeNode* root) {
        ans = 1;
        dfs(root);
        return ans - 1;
    }

    int dfs(TreeNode * node) {
        if(!node) return 0;
        int left = dfs(node->left);
        int right = dfs(node->right);
        ans = max(ans, left + right + 1);
        return max(left, right) + 1;
    }
};
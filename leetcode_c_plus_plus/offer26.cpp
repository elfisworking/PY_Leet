// 剑指 Offer 26. 树的子结构
// https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer26.cpp
@Time : 2021/12/05 18:37:38
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
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        if(A == NULL || B == NULL) return false;
        queue<TreeNode *> q;
        q.push(A);
        while(!q.empty()) {
            TreeNode * node = q.front();
            q.pop();
            if(node->val == B->val && check(node, B)) return true;
            if(node->left != NULL) q.push(node->left);
            if(node->right != NULL) q.push(node->right);
        }
        return false;

    }

    bool check(TreeNode * A, TreeNode * B) {
        if(A == NULL && B != NULL) return false;
        if(B == NULL) return true;
        if(A->val != B->val) return false;
        return check(A->left, B->left) && check(A->right, B->right);
    }
};
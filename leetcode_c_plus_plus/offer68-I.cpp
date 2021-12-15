// 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
// https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
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
@File : offer68-I.cpp
@Time : 2021/12/14 20:49:10
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking : 深度遍历，记录路径，找到共同的祖先 但是没有利用二叉搜索树的性质。 或者利用二插树的性质。
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
    TreeNode * ans = NULL;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL) return NULL;
        if(p->val > q->val) {
            TreeNode * tmp = p;
            p = q;
            q = tmp;
        }
        find(root, p, q);
        return ans;
        
    }

    void find(TreeNode * node, TreeNode *p , TreeNode *q) {
        if(node == NULL) return;
        if(p->val <= node->val && node->val <= q->val) {
            ans = node;
            return;
        }
        if(q->val < node->val) find(node->left, p, q);
        else find(node->right, p, q);
    }

};
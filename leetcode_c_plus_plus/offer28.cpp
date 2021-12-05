// 剑指 Offer 28. 对称的二叉树
// https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
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
@File : offer28.cpp
@Time : 2021/12/05 18:47:02
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
    bool isSymmetric(TreeNode* root) {  
        if(!root) return true;
        return check(root->left, root->right);
    }

    bool check(TreeNode * left,  TreeNode * right) {
        if(left == NULL && right == NULL) return true;
        if(left && right) {
            if(left->val == right->val) return check(left->left, right->right) && check(left->right, right->left);
            return false;
        }
        return false;
    }
};
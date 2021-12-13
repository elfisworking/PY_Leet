// 剑指 Offer 55 - II. 平衡二叉树
// https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
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
@File : offer55-II.cpp
@Time : 2021/12/13 19:31:50
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
    bool isBalanced(TreeNode* root) {
        if(root == NULL) return true;
        else return abs(depth(root->left) - depth(root->right)) <= 1 && isBalanced(root->left) && isBalanced(root->right);
    
        
    }

    int depth(TreeNode * node) {
        if(node == NULL) return 0;
        int left = depth(node->left);
        int right = depth(node->right);
        return  max(left, right) + 1;
    }
};
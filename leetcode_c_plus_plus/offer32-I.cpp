// 剑指 Offer 32 - I. 从上到下打印二叉树
// https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
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
@File : offer32-I.cpp
@Time : 2021/12/05 21:09:55
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

    vector<int> levelOrder(TreeNode* root) 
    {
        if(!root)
        {
            return {};
        }
        
        vector<int> res;
        iQueue.push(root);
        while(!iQueue.empty())
        {
            auto tmp = iQueue.front();
            res.push_back(tmp->val);
            
            if(tmp->left)
            {
                iQueue.push(tmp->left);
            }
            if(tmp->right)
            {
                iQueue.push(tmp->right);
            }
            iQueue.pop();
        }
        return res;
    }

private:
    queue<TreeNode*> iQueue;
};

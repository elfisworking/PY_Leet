// 剑指 Offer 32 - III. 从上到下打印二叉树 III
// https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
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
@File : offer31-III.cpp
@Time : 2021/12/05 20:59:48
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
    vector<vector<int>> levelOrder(TreeNode* root) 
    {
        if(!root)
            return {};

        vector<vector<int>> res;
        
        iQueue.push(root);
        bool flag = true;
        while(!iQueue.empty())
        {
            vector<int> levelVec;
            // 遍历每层节点数量次
            for(int i = iQueue.size(); i > 0; --i)
            {
                auto topNode = iQueue.front();
                if(flag)
                    levelVec.push_back(topNode->val);
                else
                    levelVec.insert(levelVec.begin(), topNode->val);
                iQueue.pop();
                if(topNode->left)
                    iQueue.push(topNode->left);
                if(topNode->right)
                    iQueue.push(topNode->right);
            }
            res.push_back(levelVec);
            flag = !flag;
        }
        return res;
    }
private:
    queue<TreeNode*> iQueue;
};
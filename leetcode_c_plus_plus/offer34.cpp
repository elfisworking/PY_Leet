// 剑指 Offer 34. 二叉树中和为某一值的路径
// https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
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
@File : offer34.cpp
@Time : 2021/12/10 16:28:02
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

class Solution {
public:
   vector<vector<int>> res;
   void bl(TreeNode* root, int& target,vector<int>& temp)
   {
       if(root == nullptr)return;
       target  -= root->val;
       temp.push_back(root->val);
       if(target == 0&& root->right == nullptr&&root->left == nullptr)
       {
           res.push_back(temp);
           
       }

       bl(root->left,target,temp);
       bl(root->right,target,temp);
       target += root->val;
       temp.pop_back();
   }


    vector<vector<int>> pathSum(TreeNode* root, int target) {
    vector<int> temp;
    bl(root,target,temp);
    return res;
    }
};


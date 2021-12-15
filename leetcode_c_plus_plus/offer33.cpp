// 剑指 Offer 33. 二叉搜索树的后序遍历序列
// https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
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
@File : offer33.cpp
@Time : 2021/12/15 14:13:47
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
class Solution {
public:
    bool verifyPostorder(vector<int>& postorder) {
        return curr(0, postorder.size() - 1, postorder);
    }

    bool curr(int left ,int right, vector<int>& postorder) {
        if(left >= right) return true;
        int m = left;
        while(postorder[m] < postorder[right]) m++;
        int p = m;
        while(postorder[p] > postorder[right]) p++;
        return p == right && curr(left, m - 1, postorder) && curr(m, p - 1, postorder);
    }
};
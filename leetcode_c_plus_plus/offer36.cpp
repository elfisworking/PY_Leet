// 剑指 Offer 36. 二叉搜索树与双向链表
// https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
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
@File : offer36.cpp
@Time : 2021/12/13 21:05:10
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if(root == NULL) return NULL;
        queue<Node *> s;
        Node * pre = NULL;
        Node * ans = NULL;
        mid(root, s);
        while(!s.empty()) {
            if(pre == NULL) {
                pre = s.front();
                ans = pre;
                s.pop();
            }else {
                Node * node = s.front();
                node->left  = pre;
                pre->right = node;
                pre = node;
                s.pop();
            }
        }
        pre->right = ans;
        ans->left = pre;

        return ans;
    }

    void mid(Node * node, queue<Node *> & s) {
        if(node == NULL) return;
        mid(node->left, s);
        s.push(node);
        mid(node->right, s);
    }
};
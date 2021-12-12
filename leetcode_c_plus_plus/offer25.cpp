// 剑指 Offer 25. 合并两个排序的链表
// https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
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
@File : offer25.cpp
@Time : 2021/12/10 14:09:30
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(!l1 && !l2) return NULL;
        if(l2 && !l1) return l2;
        if(!l2 && l1) return l1;
        if(l2->val < l1->val) {
            ListNode * tmp = l1;
            l1 = l2;
            l2 = tmp;
        }
        //l1 merge l2
        cout << l1->val << l2->val << endl;
        ListNode * pre = NULL;
        ListNode * node1 = l1;
        ListNode * node2 = l2;
        while(node1 && node2) {
            if(node1->val > node2->val) {
                ListNode * tmp = node2->next;
                pre->next = node2;
                node2->next = node1;
                pre = node2; 
                node2 = tmp;
            }else {
                pre = node1;
                node1 = node1->next;
            }
        }
        if(node2) pre->next = node2;
        return l1;
    }
};
// 剑指 Offer 24. 反转链表
// https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer24.cpp
@Time : 2021/11/28 21:27:14
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
    ListNode* reverseList(ListNode* head) {
        ListNode * pre = nullptr;
        ListNode * tmp = nullptr;
        while(head != nullptr) {
            tmp = head->next;
            head->next = pre;
            pre = head;
            head = tmp;
        }
        return pre;

    }
};
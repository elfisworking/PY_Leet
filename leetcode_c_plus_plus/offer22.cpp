// 剑指 Offer 22. 链表中倒数第k个节点
// https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
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
@File : offer22.cpp
@Time : 2021/12/06 19:42:12
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
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode * slow = head;
        ListNode * quick = head;
        int i = 0;
        while(i < k) {
            quick = quick->next;
            i++;
        }
        while(quick) {
            quick = quick->next;
            slow = slow->next;
        }
        return slow;

    }
};
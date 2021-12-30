// https://leetcode-cn.com/problems/reverse-linked-list/
// 206. 反转链表
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
#include<unordered_map>
using namespace std;
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
/**
@File : 206.cpp
@Time : 2021/12/30 20:21:33
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag : Easy
**/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode * pre = nullptr;
        ListNode * curr = head;
        ListNode * tmp = nullptr;
        while(head) {
            tmp = head->next;
            head->next = pre;
            pre = head;
            head = tmp;
        }
        return pre;
    }
};


class Solution {

public:
    ListNode * ans;
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr) return nullptr;
        recursive(head);
        return ans;
    }

    ListNode * recursive(ListNode * head) {
        if(head->next == nullptr) {
            ans = head;
            return head;
        }
        ListNode * node = recursive(head->next);
        node->next = head;
        head->next = nullptr;
        return head;
    }
};
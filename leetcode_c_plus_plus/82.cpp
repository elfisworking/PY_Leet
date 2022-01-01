// 82. 删除排序链表中的重复元素 II
// https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
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
@File : 82.cpp
@Time : 2022/01/01 12:44:39
@Author : YuMin Zhang
@State : Indepeedent
@Thinking :
@Tag :Medium
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode * dummy = new ListNode(-101, head);
        ListNode * curr = dummy;
        while(curr && curr->next && curr->next->next) {
            if(curr->next->val == curr->next->next->val){
                while(curr->next->next && curr->next->val == curr->next->next->val) {
                    curr->next->next = curr->next->next->next;
                }
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }

        ListNode * ans = dummy->next;
        delete dummy;
        return ans;

    }
};

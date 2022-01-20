//
//
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
@File : 02.05.cpp
@Time : 2022/01/19 22:35:27
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
**/
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* dummy=new ListNode(0);//哑节点
        ListNode* cur=dummy;
        int add=0;
        while(l1||l2||add){
            add+=(l1?l1->val:0)+(l2?l2->val:0);//进位的值+l1节点值+l2节点值
            cur->next=new ListNode(add%10);//当前节点的值 add%10
            add/=10;//获得进位的值 add/10
            cur=cur->next;
            l1=l1?l1->next:nullptr;//l1移动下一个节点(如果不为空)
            l2=l2?l2->next:nullptr;//l2移动下一个节点(如果不为空)
        }
        return dummy->next;
    }
};
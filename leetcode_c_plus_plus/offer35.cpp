// 剑指 Offer 35. 复杂链表的复制
// https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
#include<map>
#include<set>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;
#define INT_MAX 2147483637
#define INT_MIN (-INT_MAX - 1)
/**
@File : offer35.cpp
@Time : 2021/11/28 21:48:55
@Author : YuMin Zhang
@State : Indepeedent | Depedent | Half-Depedent
@Thinking :
**/

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:

    Node* copyRandomList(Node* head) {
       unordered_map<Node *, Node *> map;
       Node * ans = head;
       while(head) {
           Node * newHead = nullptr;
           Node * nextNode = nullptr;
           Node * randNode = nullptr;
           if(!map.count(head)) {
               newHead = new Node(head->val);
               map[head] = newHead;
           }else {
               newHead = map[head];
           }

           if(head->next && !map.count(head->next)) {
               nextNode = new Node(head->next->val);
               map[head->next] = nextNode;
           }else{
               if(head->next)
               nextNode = map[head->next];
           }

           if(head->random && !map.count(head->random)){
               randNode = new Node(head->random->val);
               map[head->random] = randNode;
           } else {
               if(head->random)
               randNode = map[head->random];
           }
           newHead->next = nextNode;
           newHead->random = randNode;
           head = head->next;
       } 
       return map[ans];
        
    }
};
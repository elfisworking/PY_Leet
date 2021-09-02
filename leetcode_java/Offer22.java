package leetcode_java;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Offer22{
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode slow = head;
        for(int i = 0; i < k; i++){
            head = head.next;
        }
        while(head != null){
            head = head.next;
            slow = slow.next;
        }
        return slow;

    }
}
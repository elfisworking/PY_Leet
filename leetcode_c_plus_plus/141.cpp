using namespace std;
#include <vector>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        if(head == NULL || head->next == NULL){
            return false;
        }
        ListNode * slow = head ;
        ListNode * fast = head->next;
        while(fast != NULL){
            slow = slow->next;
            if(fast->next == NULL){
                return false;
            }
            fast = fast->next->next;
            if(slow == fast){
                return true;
            }
        }
        return false;
        
    }
};
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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* dummyNode=new ListNode(0);
        ListNode* newcur=dummyNode;
        ListNode* cur=head;
        while(1)
        {
            int s=0;
            while(cur->next!=nullptr && cur->next->val!=0)
            {
                cur=cur->next;
                s=s+cur->val;
            }
            newcur->next=new ListNode(s);
            newcur=newcur->next;
            cur=cur->next;
            if(cur->next==nullptr) break;
        }
        ListNode* newHead=dummyNode->next;
        delete(dummyNode);
        return newHead;
    }
};
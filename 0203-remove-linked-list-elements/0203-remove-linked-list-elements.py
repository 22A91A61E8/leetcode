# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        
        while curr:
            next_node=curr.next
            if curr.val==val:
                prev.next=next_node
            else:
                prev=curr
            curr=next_node
        return dummy.next
    
       
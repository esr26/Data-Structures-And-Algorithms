# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        

        slow = fast = head
        tmp = None

        for _ in range(n):
            fast = fast.next
        
        while fast:
            tmp = slow
            slow = slow.next
            fast = fast.next
        
        if tmp:
            tmp.next = slow.next
            slow = None
        else:
            return slow.next
        return head

        
        

        
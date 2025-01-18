# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = curr = ListNode(-1)
        c = 0
        while l1 or l2:
            if l1 and l2:
                new_val = l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next
            elif l1:
                new_val = l1.val + c
                l1 = l1.next
            else:
                new_val = l2.val + c
                l2 = l2.next

            r = new_val % 10
            c = new_val//10

            curr.next = ListNode(r)
            curr = curr.next
            
        if c > 0:
            curr.next = ListNode(c)
        
        return dummy.next

            


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next: return head

        s_tmp = f_tmp = prev = None
        slow = head
        fast = final = head.next

        while slow and fast:
            
            s_tmp = fast.next
            if fast.next:
                f_tmp = fast.next.next

            slow.next = fast.next
            fast.next = slow

            if prev:
                prev.next = fast

            prev = slow
            slow = s_tmp
            fast = f_tmp
        
        return final
        
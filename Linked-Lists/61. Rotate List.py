# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next: return head

        cnt = 0
        n = head
        while n:
            cnt += 1
            n = n.next
        
        k%=cnt

        if k == 0: return head

        dummy = ListNode(-1)
        dummy.next = head

        fast = head
        for _ in range(k):
            fast = fast.next
        
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        tmp = dummy.next
        dummy.next = slow.next
        fast.next = tmp
        slow.next = None

        return dummy.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        res = head
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return res.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if not slow.next:
            return None
        
        slow.next = slow.next.next

        return head
        

        # 1 2 3 4 5
        # 5
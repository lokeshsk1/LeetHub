# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start = head
        middle = self.middle(head)
        rev = self.reverse(middle)
        res = ListNode(-1)
        res2 = res

        while rev:
            
            if start != middle:
                res.next = start
                start = start.next
                res = res.next

            res.next = rev
            rev = rev.next
            res = res.next
        

    def middle(self, head):

        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverse(self, head):

        prev = None

        while head:

            nxt = head.next
            head.next = prev

            prev = head
            head = nxt
        
        return prev

        
        
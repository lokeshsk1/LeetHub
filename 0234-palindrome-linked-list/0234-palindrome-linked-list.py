# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        start = head
        middle = self.middle(head)
        rev = self.reverse(middle)

        while rev:
            if start.val != rev.val:
                return False
            start = start.next
            rev = rev.next
        
        return True


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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        head_orig = head
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # print(slow)
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            nxt = curr.next

            curr.next = prev
            prev = curr
            curr = nxt

        left = head_orig
        right = prev

        # print(left)
        # print(right)

        
        res_dummy = ListNode(0)
        res = res_dummy

        while left and right:
            res.next = left
            res = res.next
            left = left.next

            res.next = right
            res = res.next
            right = right.next

            # print(res_dummy, left, right)
            # print("***")

        if left:
            res.next = left
            res = res.next
            res.next = None

        return res_dummy.next
        
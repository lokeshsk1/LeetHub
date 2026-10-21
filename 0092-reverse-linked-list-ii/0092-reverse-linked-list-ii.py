# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if left == right:
            return head

        prev = head
        for _ in range(right):
            prev = prev.next

        # edge case: sublist starts at the head
        if left == 1:
            curr = head
            for _ in range(right):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev          # new head

        curr = head
        for _ in range(left - 2):
            curr = curr.next

        temp = curr
        curr = curr.next

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        temp.next = prev
        return head
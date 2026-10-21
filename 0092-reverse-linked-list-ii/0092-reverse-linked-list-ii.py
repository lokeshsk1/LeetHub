# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        if left == right:
            return head

        dummy = ListNode(0, head)

        prev = head
        for _ in range(right):
            prev = prev.next

        curr = dummy
        for _ in range(left - 1):
            curr = curr.next

        temp = curr
        curr = curr.next

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        temp.next = prev
        return dummy.next
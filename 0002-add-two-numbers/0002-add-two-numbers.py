# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tally = 0

        res = ListNode(0)
        head_res = res

        while l1 and l2:

            tot = l1.val + l2.val + tally
            tally = tot // 10
            new_tot = tot % 10
            res.next = ListNode(new_tot)

            l1 = l1.next
            l2 = l2.next
            res = res.next

        if l2:
            l1 = l2

        while l1:

            tot = l1.val + tally
            tally = tot // 10
            new_tot = tot % 10

            res.next = ListNode(new_tot)
            l1 = l1.next
            res = res.next

        if tally:
            res.next = ListNode(tally)

        print(head_res.next)
        return head_res.next
            


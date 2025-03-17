# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ListNode.__lt__ = lambda self,x : self.val < x.val

        pq = []
        res = ListNode(0)
        curr = res

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, node))
        
        while pq:
            _, node = heapq.heappop(pq)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))
            
        return res.next

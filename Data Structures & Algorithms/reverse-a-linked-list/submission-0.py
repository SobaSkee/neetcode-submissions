# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # need temp because we overwrote curr.next to previous
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev # prev is actually the head of the reversed linkedlist now, and curr is at null
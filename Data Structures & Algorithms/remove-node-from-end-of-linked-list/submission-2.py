# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # move fast n+1 steps ahead
        for i in range(n+1):
            if fast:
                fast = fast.next
        
        # move both pointers until fast reaches None
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast n+1 steps ahead so the gap between fast and slow is n
        for _ in range(n + 1):
            if fast:
                fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Delete the n-th node from the end
        slow.next = slow.next.next

        return dummy.next


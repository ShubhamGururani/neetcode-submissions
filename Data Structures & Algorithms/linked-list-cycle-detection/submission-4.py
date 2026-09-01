# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow and fast:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if fast and fast.val==slow.val and fast.next == slow.next:
                return True
            slow = slow.next
        return False
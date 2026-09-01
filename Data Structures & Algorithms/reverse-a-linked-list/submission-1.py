# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        prev = None
        while head:
            if not rev:
                rev = head
                head = head.next
                rev.next = None
            else:
                prev = rev
                rev = head
                head = head.next
                rev.next = prev
        return rev
        
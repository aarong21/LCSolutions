# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev, nex = None, None

        while curr is not None:
            # next node to switch
            nex = curr.next
            # start reversing order
            curr.next = prev
            # move prev forward to continue reversal
            prev = curr
            # move curr forward to continue reversal
            curr = nex
        return prev
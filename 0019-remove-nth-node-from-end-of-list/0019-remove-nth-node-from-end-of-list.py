# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        # set distance to find the n from end
        for i in range(n):
            if fast:
                fast = fast.next

        # pointer to n-1 node
        while fast:
            slow = slow.next
            fast = fast.next

        # remove n node
        slow.next = slow.next.next
        
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        summ = 0
        head = ListNode(0)
        temp = head
        while(l1 or l2):
            summ = 0
            if not l1:
                summ = l2.val + carry
                l2 = l2.next
            elif not l2:
                summ = l1.val + carry
                l1 = l1.next
            else:
                summ = l1.val+l2.val+carry
                carry = l1.val+l2.val+carry
                l1 = l1.next
                l2 = l2.next
            carry = summ//10
            summ = summ%10
            temp.next = ListNode(summ)
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return head.next
        
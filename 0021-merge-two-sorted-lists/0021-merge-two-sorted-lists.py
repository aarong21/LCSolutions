# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mix = ListNode()
        mix_head = mix

        while list1 and list2:
            if list1.val < list2.val:
                mix.next = list1
                mix = mix.next
                list1 = list1.next
            else:
                mix.next = list2
                mix = mix.next
                list2 = list2.next
        if list1 or list2:
            mix.next = list1 if list1 else list2
            
        return mix_head.next
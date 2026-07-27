# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        c1 = l1
        c2 = l2
        carryover = 0
        while c1 or c2:
            value = c1.val if c1 else 0
            value += c2.val if c2 else 0
            value += carryover
            print(value)
            carryover = 1 if value > 9 else 0
            value = value - 10 if value > 9 else value
            res.next = ListNode(value)
            res = res.next
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
        if carryover:
            res.next = ListNode(1)
        return dummy.next

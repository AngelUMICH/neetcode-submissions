# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #get second half of linked list and reverse order
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        curr = head
        second = prev
        while second:
            tmp1 = curr.next
            tmp2 = second.next
            curr.next = second
            second.next = tmp1
            curr = tmp1
            second = tmp2


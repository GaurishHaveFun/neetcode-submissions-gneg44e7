# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        point = curr = head
        list1 = []

        while curr:
            list1.append(curr)
            curr = curr.next
        
        l = 0
        r = len(list1) - 1

        while l <= r:

            point.next = list1[l]
            point = point.next
            point.next = list1[r]
            point = point.next
            l += 1
            r -= 1
        point.next = None

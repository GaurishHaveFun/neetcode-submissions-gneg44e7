# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list1 = []
        curr = head

        while curr:
            if curr in list1:
                return True
            else:
                list1.append(curr)
                curr = curr.next
        return False
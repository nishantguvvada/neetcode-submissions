# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        fast = slow = head
        if fast is None:
            return False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next
        # return False
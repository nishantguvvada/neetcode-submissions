# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def swap(head, k):
            left = None
            curr = head
            i = 0
            while curr and i < k:
                i += 1
                right = curr.next
                curr.next = left
                left = curr
                curr = right
            return left, head
        
        def get_kth_node(start, k):
            curr = start
            while curr and k > 1:
                curr = curr.next
                k -= 1
            return curr

        kth_node = get_kth_node(head, k)

        if not kth_node:
            return head
        
        next_head = kth_node.next
        new_head, tail = swap(head, k)
        tail.next = self.reverseKGroup(next_head, k)
        return new_head
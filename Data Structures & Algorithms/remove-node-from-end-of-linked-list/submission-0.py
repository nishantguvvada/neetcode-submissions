# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        fast = dummy
        counter = 0
        while counter != n + 1:
            fast = fast.next
            counter += 1

        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

        


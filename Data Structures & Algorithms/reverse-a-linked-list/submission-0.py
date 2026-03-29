# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # arr = []
        # while curr != None:
        #     arr.append(curr.val)
        #     curr = curr.next
        # arr = arr[::-1]
        # curr = head
        # i = 0
        # while curr != None:
        #     curr.val = arr[i]
        #     i += 1
        #     curr = curr.next
        # return head
        if not head:
            return head
        curr = temp = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        tail = head
        head = prev
        return head
        


            


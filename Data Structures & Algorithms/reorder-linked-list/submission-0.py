# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None

        #reverse list2
        prev = None
        curr2 = list2

        while curr2:
            next_node = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = next_node
        
        list1 = head
        list2 = prev

        #alter attach
        while list1 and list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2
        
        return None
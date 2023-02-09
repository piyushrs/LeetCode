# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        len_ll = 0
        temp = head
        while temp:
            len_ll += 1
            temp = temp.next
        # print(len_ll, len_ll -n)
        temp = head
        prev = head
        element_to_be_removed = len_ll - n
        if element_to_be_removed == 0:
            head = head.next
            return head
        for _ in range(0, element_to_be_removed):
            prev = temp
            temp = temp.next
            
        prev.next = temp.next
        return head
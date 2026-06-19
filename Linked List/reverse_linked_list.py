from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None
        if head.next == None:
            return head
        curr = head
        next_n = None
        prev_n = None
        while curr.next != None:
            next_n = curr.next
            curr.next = prev_n
            prev_n = curr
            curr = next_n
        curr.next = prev_n
        head = curr
        return head
            
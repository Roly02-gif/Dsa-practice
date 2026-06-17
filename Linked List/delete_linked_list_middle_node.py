from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        tot_nodes = 1
        node = head
        while node.next != None:
            tot_nodes += 1
            node = node.next
        node = head
        for i in range((tot_nodes//2)-1):
            node = node.next
        middle_node = node.next
        node.next = middle_node.next
        middle_node.next = None
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node: ListNode = head
        if node == None:
            return None
        cur = None
        while node.next != None:
            next_node = node.next
            node.next = cur
            cur = node
            node = next_node
        node.next = cur
        return node
        
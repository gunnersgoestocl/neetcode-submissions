# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        is_visited = set()
        node = head
        is_visited.add(head)
        while head.next != None:
            print(is_visited)
            if head.next in is_visited:
                return True
            is_visited.add(head.next)
            head = head.next
        return False
        
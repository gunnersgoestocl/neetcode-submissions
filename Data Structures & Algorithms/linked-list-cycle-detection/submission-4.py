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
        is_visited.add(node)
        while node.next != None:
            # print(is_visited)
            if node.next in is_visited:
                return True
            is_visited.add(node.next)
            node = node.next
        return False
        
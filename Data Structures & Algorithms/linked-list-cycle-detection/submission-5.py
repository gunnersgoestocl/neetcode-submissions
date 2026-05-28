# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        is_visited = set()
        node = head
        while node != None:
            # print(is_visited)
            if node in is_visited:
                return True
            is_visited.add(node)
            node = node.next
        return False
        
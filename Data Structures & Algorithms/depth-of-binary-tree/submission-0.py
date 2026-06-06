# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [(root,1)]
        d = 1
        ans = 1
        while len(queue) > 0:
            node, d = queue.pop()
            print(d, ans)
            if node.left == None and node.right == None:
                ans = max(ans,d)
                continue
            if node.left != None:
                queue.append((node.left, d+1))
            if node.right != None:
                queue.append((node.right, d+1))
        return ans
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        elif p.val != q.val:
            return False
        qp = [p]
        qq = [q]
        while len(qp) > 0:
            np = qp.pop()
            nq = qq.pop()
            if np.left != None and nq.left != None:
                if np.left.val != nq.left.val:
                    # print("point1", np.left.val, "!=", nq.left.val)
                    return False
                qp.append(np.left)
                qq.append(nq.left)
            elif np.left != None or nq.left != None:
                return False
            if np.right != None and nq.right != None:
                if np.right.val != nq.right.val:
                    # print("point2", np.right.val, "!=", nq.right.val)
                    return False
                qp.append(np.right)
                qq.append(nq.right)
            elif np.right != None or nq.right != None:
                return False
        return True
            



        
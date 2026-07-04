# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        qr = [root]
        while len(qr) > 0:
            nr = qr.pop()
            if nr.val == subRoot.val:
                qr2 = [nr]
                qs = [subRoot]
                isSame = True
                while len(qs) > 0:
                    nr2 = qr2.pop()
                    ns = qs.pop()
                    if nr2.left != None and ns.left != None:
                        if nr2.left.val != ns.left.val:
                            isSame = False
                            break
                        else:
                            qr2.append(nr2.left)
                            qs.append(ns.left)
                    elif nr2.left != None or ns.left != None:
                        isSame = False
                        break
                    if nr2.right != None and ns.right != None:
                        if nr2.right.val != ns.right.val:
                            isSame = False
                            break
                        else:
                            qr2.append(nr2.right)
                            qs.append(ns.right)
                    elif nr2.right != None or ns.right != None:
                        isSame = False
                        break
                if isSame:
                    return True
            if nr.left != None:
                qr.append(nr.left)
            if nr.right != None:
                qr.append(nr.right)
        return False
                    
                        
        
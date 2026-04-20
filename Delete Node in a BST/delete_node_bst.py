class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    @classmethod
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is not None:
                cur = root.left
                while cur.right is not None:
                    cur = cur.right
                cur.right = root.right
                return root.left
            return root.right
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []

        def inorderTrav(root):
            if root is None:
                return

            inorderTrav(root.left)
            sortedArr.append(root.val)
            inorderTrav(root.right)
        
        inorderTrav(root)
        return sortedArr[k-1]

        
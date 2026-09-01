# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #input: root of the binary tree, output = integer
        #plan: check for the edge case if root is none return 0
        #base case: if root is none return 0
        #find the depth/length of left child and right child and compare
        #leftDepth = 1 + maxDepth(root.left)
        #return the longest length

        if root is None:
            return 0

        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))


        
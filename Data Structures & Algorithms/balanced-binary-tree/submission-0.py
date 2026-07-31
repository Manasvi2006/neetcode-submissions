# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        #make a seperate dfs function for the inner recursion traversal that returns
        #balanced bool and height

        def dfs(root):
            #base case
            if root is None:
                #return true bc it is balanced and its empty so there's no height
                return [True, 0]
            else:
                #run post order to start from the very last node and go up
                left, right = dfs(root.left), dfs(root.right)

                #calculate what balanced is now at the current last node thats not empty
                #balanced is true if both left and right's balance is true and if their differene is <= 1
                balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
                #return the balance and the height which is max of left and right of that node
                return [balanced, 1 + max(left[1], right[1])]
            
            #since the problem only requires boolean just return the balance
        return dfs(root)[0]


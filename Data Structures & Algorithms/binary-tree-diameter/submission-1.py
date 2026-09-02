# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def distance(root):
            nonlocal res
            if root==None:
                return 0
            left = distance(root.left)
            right = distance(root.right)
            res = max(res, left+right)
            return 1+ max(left, right)

        # print(left_dist, right_dist)
        distance(root)
        return res
        
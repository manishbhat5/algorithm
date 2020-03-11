"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


Solution:
DFS
the diameter is the depth of the left subtree plus the depth of the right subtree
自底向上，将 depth 附加在节点上，一层层往上加直到 root
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS
# Time: O(N), N is the tree size, we visit every node once
# Space: O(N), the size of the implicit call stack during dfs
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        # the depth of root
        def dfs(root):
            if root == None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.diameter = max(self.diameter, l + r)
            return max(l, r) + 1
        
        dfs(root)
        return self.diameter
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:32:43 2017

@author: N635053
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if sum in self.graphPath(root):
            return True
        else:
            return False
    
    
    def graphPath(self,root):
        if root is not None:
            if root.left is not None and root.right is not None:
                return [item + root.val for item in (self.graphPath(root.left)+ self.graphPath(root.right))]
            elif root.left is not None:            
                return [item + root.val for item in self.graphPath(root.left)]
            elif root.right is not None:            
                return [item + root.val for item in self.graphPath(root.right)]                
            else:
                return  [root.val]
        else:
            return []
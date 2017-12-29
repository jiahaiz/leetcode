# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:02:46 2017

@author: N635053
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is not None and root.right is not None:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        elif root.left is not None:
            return self.minDepth(root.left)+1
        elif root.right is not None:
             return self.minDepth(root.right)+1
        else:
            return 1
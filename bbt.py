# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:51:52 2017

@author: USER
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if root.left is None and root.right is None:
                return True
            elif root.left is None:
                if root.right.left is None and root.right.right is None:
                    return True
                else:
                    return False
            elif root.right is None:
                if root.left.left is None and root.left.right is None:
                    return True
                else:
                    return False   
            else:
                return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
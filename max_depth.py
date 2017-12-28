# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:40:15 2017

@author: N635053
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        else:
            if (root.left==None and root.right==None):
                return 1
            elif root.left==None:
                return 1+ self.maxDepth(root.right)
            elif root.right == None:
                return 1+self.maxDepth(root.left)
            else:
                left_dept = self.maxDepth(root.left)
                right_dept = self.maxDepth(root.right)
                return 1+(left_dept if left_dept>right_dept else right_dept)
    
if __name__ == "__main__":
    s = Solution()
    a= TreeNode(1)
    b= TreeNode(2)
    c= TreeNode(3)
    a.left = b
    a.right = c
    print s.maxDepth(a) 
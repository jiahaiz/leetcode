# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:31:23 2017

@author: N635053
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        else:
            return self.isSymmeticSubTree(root.left,root.right)
                
    def isSymmeticSubTree(self,left,right):
        if(left==None and right == None):
            return True
        elif(left==None or right == None):
            return False
        else:
            if(left.val == right.val):
                return self.isSymmeticSubTree(left.left,right.right) and self.isSymmeticSubTree(left.right,right.left)
            else:
                return False
                
if __name__ == "__main__":
    s = Solution()
    a= TreeNode(1)
    b= TreeNode(2)
    c= TreeNode(3)
    a.left = b
    a.right = c
    print s.isSymmetric(a) 
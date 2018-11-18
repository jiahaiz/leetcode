# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:10:27 2017

@author: N635053
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q== None:
            return True
        elif p== None or q==None:
            return False
        else:
            if p.val!=q.val :
                return False
            else:
                if p.left != None and q.left != None and p.right != None and q.right != None:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
                elif p.left == None and q.left == None and p.right == None and q.right == None:
                    return True
                elif p.left != None and q.left != None and p.right == None and q.right == None:
                    return self.isSameTree(p.left, q.left) 
                elif p.left == None and q.left == None and p.right != None and q.right != None:
                    return self.isSameTree(p.right, q.right)
                else:
                    return False
                    
                    
if __name__ == "__main__":
    s = Solution()
    a= TreeNode(1)
    b= TreeNode(2)
    c= TreeNode(1)
    a.left = b
    a.rifht=c
    aa= TreeNode(1)
    bb= TreeNode(2)
    cc= TreeNode(1)
    aa.left = cc
    aa.rifht= bb
    print s.isSameTree(a,aa) 

    
                    
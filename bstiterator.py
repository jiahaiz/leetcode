# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:05:26 2018

@author: USER
"""
# Definition for a  binary tree node
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack =[]
        self.left_end(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack)>0:
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        result = self.stack.pop()
        if result.right is not None:
            self.left_end(result.right)
        return result.val
        
    def left_end(self,root):
        move = root
        while(move != None):
            self.stack.append(move)
            move = move.left
            
if __name__ == "__main__":
    root = TreeNode(1)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v
    
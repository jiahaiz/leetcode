# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:31:21 2017

@author: N635053
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.levelMark(result,0,root)
        result.reverse()
        return result
        
    def levelMark(self, result_list, level, root):
        if root != None:
            if level < len(result_list):
                result_list[level].append(root.val)
            else:
                result_list.append([root.val])
            self.levelMark(result_list,level+1,root.left)
            self.levelMark(result_list,level+1,root.right)
   

if __name__ == "__main__":
    s = Solution()
    a= TreeNode(3)
    b= TreeNode(9)
    c= TreeNode(20)
    d= TreeNode(15)
    e= TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    print s.levelOrderBottom(a)          
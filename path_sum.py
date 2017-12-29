# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:15:35 2017

@author: N635053
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def pathSum(self, root, sum_val):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        all_list=self.graphPath(root)
        result = []
        for item in all_list:
            if sum(item) == sum_val:
                item.reverse()
                result.append(item)
        return result
        
        
    def graphPath(self,root):
        if root is not None:
            if root.left is not None and root.right is not None:
                tmp_list =  self.graphPath(root.left)+ self.graphPath(root.right)
                [item.append(root.val) for item in tmp_list]
                return tmp_list
            elif root.left is not None: 
                tmp_list = self.graphPath(root.left)
                [item.append(root.val) for item in tmp_list]
                return tmp_list
            elif root.right is not None: 
                 tmp_list = self.graphPath(root.right)
                 [item.append(root.val) for item in tmp_list]
                 return tmp_list               
            else:
                return  [[root.val]]
        else:
            return []  
            
if __name__ == "__main__":
    s = Solution()
    a= TreeNode(1)
    b= TreeNode(2)
    c= TreeNode(1)
    a.left = b
    a.right=c
    print s.pathSum(a,3) 
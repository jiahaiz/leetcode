# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:03:54 2018

@author: USER
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    
    def findModeHelp(self,root,mode_map):
        if root is not None:
            if root.val not in mode_map:
                mode_map[root.val]=1
            else:
                mode_map[root.val]+=1
            self.findModeHelp(root.left,mode_map)  
            self.findModeHelp(root.right,mode_map) 
        
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mode_map = {}
        self.findModeHelp(root,mode_map)
        if len(mode_map)==0:
            return []
        if len(mode_map)==1:
            return mode_map.keys()
        sorted_d = sorted(mode_map.iteritems(), key=lambda (k,v): (v,k),reverse=True)
        max_v = sorted_d[0][1]
        result=[]
        for item in sorted_d:
            if item[1]==max_v:
                result.append(item[0])
            else:
                break
        return result
    
if __name__ == "__main__":
    s= Solution()
    a = TreeNode(1)
    b =TreeNode(2)
    a.right = b
    print s.findMode(a)

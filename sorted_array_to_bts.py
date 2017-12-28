# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:18:24 2017

@author: N635053
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        elif len(nums)==2:
            tmp_root= TreeNode(nums[1])
            tmp_left = TreeNode(nums[0])
            tmp_root.left =tmp_left
            return tmp_root
        elif len(nums)==3:
            tmp_right = TreeNode(nums[2])
            tmp_root= TreeNode(nums[1])
            tmp_left = TreeNode(nums[0])
            tmp_root.left =tmp_left
            tmp_root.right =tmp_right
            return tmp_root
        else:
            mid = len(nums)/2
            tmp_root= TreeNode(nums[mid])
            tmp_right=self.sortedArrayToBST(nums[mid+1:])
            tmp_left = self.sortedArrayToBST(nums[0:mid])
            tmp_root.left =tmp_left
            tmp_root.right =tmp_right
            return tmp_root
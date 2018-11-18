# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 00:26:45 2018

@author: USER
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <3:
            return max(nums)
        d=[]
        d.append( nums[0])
        d.append( max(nums[0],nums[1]))
        lenght = len(nums)
        i =2
        while(i<lenght):
            d.append( max(nums[i]+d[i-2],d[i-1]))
            i +=1
        return d[i-1]
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:11:13 2018

@author: USER
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0;
        while (n!=0):
            result += (n&1)
            n=n>>1
        return result
        
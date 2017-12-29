# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:02:29 2017

@author: N635053
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        result = []
        pre_row = []
        for i in xrange(1,1+numRows):
            if i == 1:
                pre_row= [1]
            elif i ==2:
                pre_row =[1,1]
            else:
                tmp = [1,1]
                for j in xrange(1,i-1):
                    tmp.insert(j,pre_row[j-1]+pre_row[j])
                pre_row = tmp
            result.append(pre_row)
        return result
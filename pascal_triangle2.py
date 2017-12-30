# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:25:22 2017

@author: USER
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex ==0:
            return [1]
        if rowIndex ==1:
            return [1,1]
        pre_row=[1,1]
        for i in xrange(1,rowIndex):
            tmp =[1,1]
            print i
            for j in xrange(1,i+1):
                tmp.insert(j,pre_row[j-1]+pre_row[j])
            pre_row = tmp            
        return pre_row
    
if __name__ == "__main__":
    s= Solution()
    print s.getRow(9)
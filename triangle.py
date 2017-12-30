# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:36:21 2017

@author: USER
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        triangle.reverse()
        all_path = [[i] for i in  triangle[0]]
        del triangle[0]
        for item in triangle:
            tmp =[]
            lenght= len(item)
            for i in xrange(lenght):
                tmp.append([item[i]+ min( all_path[i])]+[item[i]+min( all_path[i+1])])
            all_path =tmp
        return min(all_path[0])
        
if __name__ == "__main__":
    s= Solution()
    print s.minimumTotal([[-1],[2,3],[1,-1,-3]])            
        
            
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:52:52 2018

@author: USER
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        result = 0
        j = 0
        for i in houses:
            print j
            while(j<(len(houses)-1) and abs(heaters[j+1]-i)<=abs(heaters[j]-i)):
                j+=1
            result = max(abs(heaters[j] - i),result)
        return result

if __name__ == "__main__":
    s= Solution()
    print s.findRadius([1,2,3],[2])
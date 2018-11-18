# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:32:52 2018

@author: USER
"""

from collections import Counter

class Solution(object):
    def distance_pow2(self,p1,p2):
        return (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])
    
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<3:
            return 0
        length = len(points)
        i =0
        result = 0
        while(i<length):
            temp = list(points)
            del temp[i]
            distance_array =[]
            for item in temp:
                distance_array.append(self.distance_pow2(points[i],item))
            counter = Counter(distance_array)
            for distance_counter in counter.values():      
                if distance_counter >1:
                    result +=distance_counter*(distance_counter-1)
            i+=1    


        return result
    
if __name__ == "__main__":
    s= Solution()
    print s.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
            
       
        
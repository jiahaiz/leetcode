# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 22:49:37 2018

@author: USER
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]    
        nums.sort()
        count=0
        compare_v=0
        for i in nums:
            print i
            if count%3 ==0:
                compare_v=i
            else:
                if i!=compare_v:
                    return compare_v
            count+=1
        return nums[count-1]
    
if __name__ == "__main__":
    s= Solution()
    print s.singleNumber([2,2,3,2])
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 22:31:36 2018

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
        count = 0
        p_v = 0
        for i in nums:
            if count%2 ==0:
                p_v =i
            else:
                if p_v-i != 0:
                    return p_v
            count +=1
        return nums[count-1]
    
if __name__ == "__main__":
    s= Solution()
    print s.singleNumber([1,1,2,2,3])
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 22:13:15 2018

@author: USER
"""

def superStack(operations):
    stack = []
    for op in operations:
        array = op.split()
        
        if array[0]=="push":
            stack.append(int(array[1]))
        elif array[0]=="pop" and len(stack)>0:
            del stack[0]
        elif array[0]=="inc":
            count = int(array[1])
            add_value = int(array[2])
            i = 0
            while i < min(count,len(stack)):
                stack[i]+=add_value
                i+=1
        if len(stack)==0:
            print "EMPTY"
        else:
            print stack[-1]
            
def numSubarrayProductLessThanK( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    re = 0
    window = []
    for item in nums:
        if item < k:
            re+=1
            if len(window)>0:
                print window
                while reduce(lambda x,y:x*y,window)*item >=k:
                    del window[0]
            re+=len(window)
            window.append(item)
        else:
            window=[]
    return re
            
if __name__ =="__main__":
    numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3],19)
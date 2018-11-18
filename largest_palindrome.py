# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:02:51 2018

@author: USER
"""

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        half_number = pow(10,n)-1
        
        end_number = pow(10,n-1)
        while (half_number > end_number):
            palindrome_num = long(str(half_number)+str(half_number)[::-1])
            temp = pow(10,n)-1
            while(palindrome_num/temp < pow(10,n)-1):
                if palindrome_num%temp == 0:
                    print palindrome_num,temp
                    return palindrome_num%1337
                else:
                    temp -=1            
            half_number -=1
        return -1
            
if __name__ == "__main__":
    s= Solution()
    for i in xrange(1,9):
        s.largestPalindrome(i)
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 01:24:29 2018

@author: USER
"""

class Solution(object):
    def num2letter(self,num):
        return chr(num+64)
    
    def pre_letter(self,letter):
        if letter =="A":
            return ""
        return chr(ord(letter)-1)
    
    def convertToTitle1(self, n):
        """
        :type n: int
        :rtype: str
        """
        divide = 26
        count =0
        while n/pow(divide,count)>0:
            count +=1
        result=""
        count -=1
        while count >=0:
            tmp = n/pow(divide,count)  
            n = n- tmp*(pow(divide,count))
            if tmp != 0:
                result = result+self.num2letter(tmp)
            else:
                result = result[:-1] +self.pre_letter(result[-1])+"Z"
            count -=1   
        return result
    
    def convertToTitle(self, num):
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))
    
if __name__ == "__main__":
    s= Solution()
    #print s.convertToTitle(1)
    for i in xrange(1,100):
      print  s.convertToTitle(i)
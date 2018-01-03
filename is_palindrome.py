# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lenght = len(s)
        begin = 0
        end = lenght -1
        while begin < end:
            if(s[begin].isalnum() is False and s[end].isalnum is False):
                while s[end].isalnum() is False:
                    end -=1
                    if end==0:
                        break
                while s[begin].isalnum() is False:
                    begin +=1
                    if begin == lenght-1:
                        break
                if end <= begin:
                    break
            elif s[begin].isalnum():
                while s[end].isalnum() is False:
                    end -=1
                    if end==0:
                        break
            elif s[end].isalnum():
                while s[begin].isalnum() is False:
                    begin +=1
                    if begin == lenght-1:
                        break
                if end <= begin:
                    break
            if(s[begin].isalnum() and s[end].isalnum()):
                print s[begin],s[end]
                if s[begin].lower()  != s[end].lower() :
                    return False

            begin +=1
            end -=1
        return True
        
if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome("Sir, I'm Iris!")
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 18:10:49 2018

@author: USER
"""

import sys
class Solution(object):
    def find(self,s,item):
        count =0
        i =0
        while i<len(s):
            if s[i] !=item[i]:
                count +=1
            i+=1
        return count==1
        
        
        
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        mem ={(end,end):0}
        def help(s,e,bank):
            if s=="AAACCCCC" and e == "CCCCCCCC":
                print "1"
            if (s,e) in mem:
                return mem[(s,e)]
            else:
                ans =sys.maxint
                for item in bank:
                    if s=="AAAACCCC" and item == "AAACCCCC":
                        print "here"
                    if self.find(s,item):
                        print (s,item),bank
                        mem[(s,item)]=1
                        temp =list(bank)
                        if s in temp:
                            temp.remove(s)
                        pre = help(item,e,temp)
                        if pre != -1:
                            ans = min(ans,1+pre)
                if ans == sys.maxint:
                    mem[(s,e)]=-1
                    return -1
                else:
                    mem[(s,e)]=ans
                    return ans
        return help(start,end,bank)
    
if  __name__ == "__main__":
    s = Solution()
    a="AAAACCCC"
    b="CCCCCCCC"
    c=["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
    s.minMutation(a,b,c)
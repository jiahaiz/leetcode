# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:09:58 2017

@author: N635053
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        move = head
        while(move!=None):
            if(move.next != None):
                if(move.next.val==move.val):
                    move.next = move.next.next
                else:
                    move = move.next
            else:
                break
        return head
        
def prt(a):
    while(a!= None):
     print a.val
     a= a.next       
       
if __name__ == "__main__":
    s = Solution()
    a= ListNode(1)
    b= ListNode(1)
    c= ListNode(1)
    b.next = c
    a.next=b
    s.deleteDuplicates(c) 
    prt(c) 
    
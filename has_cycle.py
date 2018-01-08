# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 23:02:59 2018

@author: USER
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow_move = head
        fast_move = head
        while fast_move is not None:
            try:
                slow_move = slow_move.next
                fast_move = fast_move.next.next   
                if slow_move == fast_move:
                    return True
            except:
                return False
        return False
    
if __name__ == "__main__":
    s= Solution()
    a= ListNode(1)
    b=ListNode(2)
    a.next=b
    print s.hasCycle(a)
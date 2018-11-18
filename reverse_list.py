# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 09:38:35 2018

@author: USER
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def toTail(self,head):
        while head is not None:
            if head.next is not None:
                head = head.next  
            else:
                break
        return head
    
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        temp = self.reverseList(head.next)
        head.next = None
        tail = self.toTail(temp)
        tail.next = head
        return temp
    
if __name__ == "__main__":
    a = ListNode(1)
    b= ListNode(2)
    a.next = b
    s = Solution()
    print s.reverseList(a)
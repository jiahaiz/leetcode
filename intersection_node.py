# -*- coding: utf-8 -*-
"""
Created on Mon Jan 08 19:46:31 2018

@author: USER
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

import ctypes

class Solution(object):
    def id_to_value(self, id_v):
        return ctypes.cast(id_v, ctypes.py_object).value
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        address_a =[]
        address_b =[]
        move_a= headA
        move_b= headB
        while(move_a is not None):
            address_a.append(id(move_a))
            move_a= move_a.next
        while(move_b is not None):
            address_b.append(id(move_b))
            move_b= move_b.next
        print address_a, address_b               
        lenght = min(len(address_a),len(address_b))
        result = None
        count = -1
        while (-1*count) <=lenght:
             if address_a[count] == address_b[count]:
                 result = self.id_to_value(address_a[count])
             else:
                 break
             count -=1
        return result
    
if __name__ == "__main__":
    s= Solution()
    a=ListNode(1)
    print s.getIntersectionNode(a,a)
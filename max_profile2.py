# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:33:56 2017

@author: USER
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_point =0
        sell_point =1
        lenght = len(prices)
        result =0
        add_all =0
        while(sell_point<lenght):
            if prices[buy_point]>=prices[sell_point]:
                buy_point=sell_point
                add_all +=result
                result = 0
            else:
                tmp = prices[sell_point]-prices[buy_point]
                result = max(result,tmp)
            sell_point +=1 
        add_all +=result
        return add_all
    
if __name__ == "__main__":
    s= Solution()
    print s.maxProfit([7,1,5,3,6,4,6])
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
        if len(prices)<2:
            return 0
        if len(prices) == 2:
            if prices[1]>prices[0]:
                return prices[1]-prices[0]
            else: return 0
        else:
            buy_point=0
            sell_point =1
            next_sell_point =2
            result = 0
            while(next_sell_point<=len(prices)):
                if prices[buy_point]>=prices[sell_point]:
                    buy_point = sell_point
                    sell_point = next_sell_point
                    next_sell_point +=1
                else:
                    if prices[next_sell_point]<prices[sell_point]:
                        result += prices[sell_point]-prices[buy_point]
                        buy_point = next_sell_point
                        sell_point =buy_point+1
                        next_sell_point = sell_point+1
                    else:
                        sell_point = next_sell_point
                        next_sell_point +=1
                if(sell_point == len(prices)-1):
                    if prices[sell_point]>prices[buy_point]:
                        result += prices[sell_point]-prices[buy_point]
                    break
            return result
    
if __name__ == "__main__":
    s= Solution()
    print s.maxProfit([2,1,4])
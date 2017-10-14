"""
Function: Reverse digits of an integer. 
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
Example: 321 ->123, -123 -> -321 
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            a = list(str(x))
            del(a[0])
            sum = 0
            for index,number in enumerate(a):
                sum = sum + int(number)*10**index
            if 1<=sum and sum <=2**31:
                return -sum
            else:
                return 0
        else:
            b = list(str(x))
            sum = 0
            for index,number in enumerate(b):
                sum = sum + int(number)*10**index
            if 0<=sum and sum <=2**31-1:
                return sum
            else:
                return 0
             

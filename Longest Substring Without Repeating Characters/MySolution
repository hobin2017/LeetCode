import string
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length=0
        total_length =len(s)
        for test_length in range(1,total_length+1):
            for i in range(0,total_length-test_length+1):
                self.test=s[i:i+test_length]
                if self.testOfNonRepeat():
                    max_length = test_length
                    break
            if max_length != test_length:
                break
            else:
                continue
        return max_length
    
    def testOfNonRepeat(self):
        a = list(self.test)  
        n = len(a)  
        for i in range(n):  
            if self.test.count(a[i]) != 1:   
                return False  
                #break  
        return True

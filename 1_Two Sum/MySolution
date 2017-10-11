class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.total_len = len(nums)
        for i in range(self.total_len):
            sub_target = target - nums[i]
            for j in range(i+1,self.total_len):
                if sub_target == nums[j]:
                    self.index1 =i
                    self.index2 =j
                    return [self.index1,self.index2]

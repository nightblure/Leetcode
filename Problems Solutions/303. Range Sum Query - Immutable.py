# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums):
        # calc prefix sums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        self.nums = nums
        print(nums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return self.nums[right] - self.nums[left - 1]

numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2) # return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5) #return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
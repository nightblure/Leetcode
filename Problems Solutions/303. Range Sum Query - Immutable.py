# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums):
        print(nums)

        # calc prefix sums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        self.nums = nums
        print(nums)

    def sumRange(self, left: int, right: int) -> int:
        lsum = self.nums[left]
        rsum = self.nums[right]

        if left == 0:
            return rsum
        else:
            return rsum - self.nums[left - 1]

numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2) # return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5) #return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
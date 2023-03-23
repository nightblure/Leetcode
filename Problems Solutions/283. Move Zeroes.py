# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums):
        zero_pointer = 0

        for idx, num in enumerate(nums):
            if num != 0:
                nums[idx], nums[zero_pointer] = nums[zero_pointer], nums[idx]
                zero_pointer += 1

        return nums

tests_data = [
    ([0,1,0,3,12], [1,3,12,0,0])
]

obj = Solution()

for data in tests_data:
    assert obj.moveZeroes(data[0]) == data[-1]
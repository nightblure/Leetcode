# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
Вернуть сортированный массив с index + 1 двух чисел, дающих в сумме target
"""

class Solution:
    def twoSum(self, nums, target):
        l, r = 0, len(nums) - 1

        while l < r:
            ln, rn = nums[l], nums[r]
            summ = ln + rn

            if summ == target:
                return [l + 1, r + 1]
            
            if summ > target:
                r -= 1
            else:
                l += 1
            
        return []

tests_data = [
    ([2,7,11,15], 9, [1,2]),
    ([2,3,4], 6, [1,3]),
    ([-1,0], -1, [[1,2]]),

]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    result = obj.twoSum(*data[:-1])
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        mem = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in mem:
                return [index, mem[diff]]

            mem[num] = index

        return []

tests_data = [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),

]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    result = obj.twoSum(*data[:-1])
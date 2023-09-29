# https://leetcode.com/problems/3sum/

"""
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# time complexity is nlogn + n^2 = n^2
class Solution:
    def threeSum(self, nums):
        result = set()
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                total_sum = nums[l] + nums[r] + n

                if total_sum == 0:
                    result.add((n, nums[l], nums[r]))
                
                if total_sum > 0:
                    r -= 1
                else:
                    l += 1

        return list(result)

tests_data = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),

]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    result = obj.threeSum(data[0])
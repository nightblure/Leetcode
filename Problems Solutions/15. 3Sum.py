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
        def get_triplets(exclude_idx, nums, target):
            res = set()
            l, r = exclude_idx + 1, len(nums) - 1

            while l < r:
                l_num = nums[l]
                r_num = nums[r]
                summ = l_num + r_num

                if target == summ:
                    res.add(tuple([nums[exclude_idx], l_num, r_num]))

                if summ < target:
                    l += 1
                else:
                    r -= 1

            return res

        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            
            result.extend(get_triplets(i, nums, 0 - num))
        
        return result

tests_data = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),

]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    result = obj.threeSum(data[0])
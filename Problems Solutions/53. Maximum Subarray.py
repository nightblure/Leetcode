# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums) -> int:
        max_ = cur_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_ = max(max_, cur_sum)

        return max_

tests_data = (
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23)

)
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.maxSubArray(data[0])
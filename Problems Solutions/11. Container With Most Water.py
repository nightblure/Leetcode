# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0

        while l < r:
            lh, rh = height[l], height[r]
            h = min(lh, rh)
            w = r - l
            maxarea = max(maxarea, h * w)

            if lh > rh:
                r -= 1
            else:
                l += 1

        return maxarea

tests_data = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1, 1], 1)
]
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.maxArea(data[0])
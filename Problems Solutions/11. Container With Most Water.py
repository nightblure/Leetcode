# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            lh, rh = height[l], height[r]
            area = (r - l) * min(lh, rh)
            max_area = max(max_area, area)

            if lh < rh:
                l += 1
            else:
                r -= 1
        
        return max_area

tests_data = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1, 1], 1)
]
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.maxArea(data[0])
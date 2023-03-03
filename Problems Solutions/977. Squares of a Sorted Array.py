# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):
        l = 0 
        r = write_index = len(nums) - 1
        result = [0] * len(nums)

        while l <= r:
            l_num, r_num = nums[l] ** 2, nums[r] ** 2

            if l_num > r_num:
                result[write_index] = l_num
                l += 1
            else:
                result[write_index] = r_num
                r -= 1
            
            write_index -= 1
        
        return result

tests_data = [
    ([-4,-1,0,3,10], [0,1,9,16,100]),
    ([-7,-3,2,3,11], [4,9,9,49,121]),
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    assert expected == obj.sortedSquares(data[0])
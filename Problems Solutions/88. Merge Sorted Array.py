# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        p1, p2 = m - 1, n - 1
        write_pointer = n + m - 1

        while p1 >= 0 and p2 >= 0:
            n1, n2 = nums1[p1], nums2[p2]

            if n1 > n2:
                nums1[write_pointer] = n1
                p1 -= 1
            else:
                nums1[write_pointer] = n2
                p2 -= 1 
            
            write_pointer -= 1
        
        # дописываем не обработанные циклом элементы из nums2 в nums1
        while p2 >= 0:
            nums1[write_pointer] = nums2[p2]
            write_pointer -= 1
            p2 -= 1

        return nums1
    
tests_data = [
    ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    assert expected == obj.merge(*data[:-1])
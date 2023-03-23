# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = [intervals[0]]

        def merge(i1, i2):
            if i1[1] < i2[0]:
                return None
            
            if i1[0] <= i2[0] and i1[1] >= i2[1]:
                return i1
            
            return [i1[0], i2[1]]

        for i in range(1, len(intervals)):
            i1, i2 = result.pop(), intervals[i]
            merged = merge(i1, i2)

            if not merged:
                result.extend([i1, i2])
            else:
                result.append(merged)

        return result

tests_data = (
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]])

)
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.merge(data[0])
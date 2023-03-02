# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        counts_ = defaultdict(list)

        for num in counts:
            count = counts[num]
            counts_[count].append(num)

        result = []

        scounts = list(sorted(counts_.keys()))

        for i in range(len(scounts)):
            result.extend(counts_[scounts[-1 - i]])

            if len(result) == k:
                return result

tests_data = [
    ([1,1,1,2,2,3], 2, [1, 2]),
    ([1], 1, [1])
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    assert expected == obj.topKFrequent(*data[:-1])
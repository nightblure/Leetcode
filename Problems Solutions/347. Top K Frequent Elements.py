# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        counts= Counter(nums)
        freqs = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            freqs[count].append(num)

        print(freqs)
        result = []

        for i in range(len(freqs) - 1, -1, -1):
            for num in freqs[i]:
                result.append(num)

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
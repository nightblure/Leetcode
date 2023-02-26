# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

from collections import defaultdict


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = l = 0
        ss = defaultdict(int)

        for r in range(len(s)):
            ss[s[r]] += 1

            if r - l + 1 == 3:
                if len(ss) == 3:
                    count += 1

                ss[s[l]] -= 1
                if ss[s[l]] == 0:
                    del ss[s[l]]
               
                l += 1

        return count


tests_data = {
    'xyzzaz': 1, 
    'aababcabc': 4,
}
obj = Solution()

for str in tests_data:
    expected = tests_data[str]
    assert expected == obj.countGoodSubstrings(str)
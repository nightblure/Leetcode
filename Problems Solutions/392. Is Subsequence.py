# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = i1 = i2 = 0

        while i1 < len(s) and i2 < len(t):

            if s[i1] == t[i2]:
                counter += 1
                i1 += 1
                i2 += 1
            else:
                i2 += 1

            if counter == len(s):
                return True

        return counter == len(s)

tests_data = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    assert expected == obj.isSubsequence(data[0], data[1])
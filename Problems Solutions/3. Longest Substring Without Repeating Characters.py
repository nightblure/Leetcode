# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = l = 0
        ss = set()

        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1

            ss.add(s[r])
            maxl = max(maxl, r - l + 1)

        return maxl

tests_data = {
    'abcabcbb': 3, 
    'bbbbb': 1,
    'pwwkew': 3
}
obj = Solution()

for str in tests_data:
    expected = tests_data[str]
    assert expected == obj.lengthOfLongestSubstring(str)
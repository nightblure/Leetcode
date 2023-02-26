""" 
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

точно такая же задача, но в условии K символов: 
    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""
# Given a string s, return the length of the longest substring that contains at most two distinct characters.

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        K = 2
        ss = defaultdict(int)
        l = maxl = 0

        for r in range(len(s)):
            ss[s[r]] += 1

            # пока в мапе больше двух ключей, то есть больше двух уникальных символов,
            # удаляем левый символ, чтобы удовлетворять условию "most two distinct characters"
            while len(ss) > K:
                ss[s[l]] -= 1
                if ss[s[l]] == 0:
                    del ss[s[l]]
                l += 1
            
            maxl = max(maxl, r - l + 1)
        
        return maxl

tests_data = {
    'eceba': 3, 
    'ccaabbb': 5
}
obj = Solution()

for str in tests_data:
    expected = tests_data[str]
    assert expected == obj.lengthOfLongestSubstringTwoDistinct(str)
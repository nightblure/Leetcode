# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = (1, i)
            else:
                d[ch] = (d[ch][0] + 1, i)
        
        for ch, value in d.items():
            if value[0] == 1:
                return value[1]

        return -1

tests_data = {
    'leetcode': 0, 
    'loveleetcode': 2,
    'aabb': -1
}
obj = Solution()

for str in tests_data:
    expected = tests_data[str]
    assert expected == obj.firstUniqChar(str)
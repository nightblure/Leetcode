# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_repeats_count = {}

        for i, ch in enumerate(s):
            _, repeats = char_to_repeats_count.get(ch, (i, 0))
            repeats += 1
            char_to_repeats_count[ch] = (i, repeats)

        for idx, repeats_count in char_to_repeats_count.values():
            if repeats_count == 1:
                return idx

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

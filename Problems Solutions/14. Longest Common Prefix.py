# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        stop = False
        prefix = ''

        for index, ch in enumerate(strs[0]):
            for word in strs[1:]:
                if index > len(word) - 1 or ch != word[index]:
                    stop = True
                    break

            if stop:
                break
                
            prefix += ch
                
        return prefix

tests_data = [
    (["flower","flow","flight"], 'fl'),
    (["dog","racecar","car"], '')
]
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.longestCommonPrefix(data[0])
# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 0
        flag = False
        prefix = ''

        for ch in strs[0]:
            for word in strs[1:]:
                if index > len(word) - 1 or strs[0][index] != word[index]:
                    flag = True
                    break

            if flag:
                break
                
            prefix += strs[0][index]
            index += 1
                
        return prefix

tests_data = [
    (["flower","flow","flight"], 'fl'),
    (["dog","racecar","car"], '')
]
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.longestCommonPrefix(data[0])
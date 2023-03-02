# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_pal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # делаем + 1, т.к. последняя итерация цикла изменила l и r
            return s[l + 1: r]
        
        result = ''

        for i in range(len(s)):
            # поиск палиндрома с центром из одной буквы (babad)
            p1 = get_pal(i, i)
            # поиск палиндрома с центром из двух букв (cbbd)
            p2 = get_pal(i, i + 1)

            if len(p1) > len(result):
                result = p1
            if len(p2) > len(result):
                result = p2

        return result

tests_data = {
    'babad': 'bab', 
    'cbbd': 'bb'
}
obj = Solution()

for str in tests_data:
    expected = tests_data[str]
    assert expected == obj.longestPalindrome(str)
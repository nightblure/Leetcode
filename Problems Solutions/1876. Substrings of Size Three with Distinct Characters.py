# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

from collections import defaultdict


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substr = defaultdict(int)
        res = 0
        l = 0

        # хешмапа будет имитировать подстроку в скользящем окне
        # ключ - символ строки, значение - количество вхождений
        for r, ch in enumerate(s):
            substr[ch] += 1

            # если это условие истинно, то подстрока длиной 3 набрана
            # и необходимо посмотреть количество ключей (уникальных символов) в мапе
            # если оно = 3, то подстрока найдена
            # также в конец не забываем сместить скользящее окно, удалив левый символ
            if r - l + 1 == 3:
                if len(substr) == 3:
                    res += 1

                substr[s[l]] -= 1

                if substr[s[l]] == 0:
                    del substr[s[l]]
                
                l += 1     
        
        return res


tests_data = {
    'xyzzaz': 1, 
    'aababcabc': 4,
}
obj = Solution()

for str in tests_data:
    expected = tests_data[str]
    assert expected == obj.countGoodSubstrings(str)
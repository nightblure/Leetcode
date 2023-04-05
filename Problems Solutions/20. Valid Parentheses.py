# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            else:
                if not stack:
                    return False

                last_open_bracket = stack.pop()
                close_bracket = bracket
                
                if brackets[close_bracket] != last_open_bracket:
                    return False
        
        return len(stack) == 0

tests_data = [
    ('()', True),
    ('()[]{}', True),
    ('([', False)
]
obj = Solution()

for data in tests_data:
    assert data[-1] == obj.isValid(data[0])
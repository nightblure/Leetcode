# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operations = {
            '+': (lambda a, b: a + b),
            '-': (lambda a, b: a - b),
            '/': (lambda a, b: int(a / b)),
            '*': (lambda a, b: a * b),
        }

        for token in tokens:
            if token not in ('+/*-'):
                stack.append(int(token))
            else:
                operator = token
                r, l = stack.pop(), stack.pop()
                stack.append(operations[operator](l, r))

        return stack.pop()

tests_data = [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    assert expected == obj.evalRPN(*data[:-1])
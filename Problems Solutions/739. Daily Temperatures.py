# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]

            while stack and stack[-1][0] <= t:
                stack.pop()

            if stack:
                result[i] = stack[-1][1] - i
            else:
                result[i] = 0

            stack.append((t, i))

        return result

tests_data = [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0])
]
obj = Solution()

for data in tests_data:
    expected = data[-1]
    assert expected == obj.dailyTemperatures(*data[:-1])
# https://leetcode.com/problems/daily-temperatures/

"""
Идея решения: будем хранить в доп. памяти максимальные температуры на текущий момент
Максимальная температура будет расположена раньше, чем какая-то другая, и поэтому точно нам подходит
Если t1 > target_t, а некая t_max > t1, то t_max точно подойдет 
"""

class Solution:
    def dailyTemperatures(self, temps):
        result = [0] * len(temps)
        memory = [(temps[-1], len(temps) - 1)]

        for i in range(len(temps) - 2, -1, -1):
            t_cur = temps[i]

            while memory and memory[-1][0] <= t_cur:
                 memory.pop()

            if not memory:
                result[i] = 0
            else:
                t_next, index = memory[-1]
                result[i] = index - i

            memory.append((t_cur, i))

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
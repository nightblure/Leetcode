# https://leetcode.com/problems/climbing-stairs/description/

"""
Задача: 

Вы поднимаетесь по лестнице. Требуется n шагов, чтобы добраться до вершины.
Каждый раз вы можете подняться на 1 или 2 ступеньки. 
Сколькими различными способами вы можете подняться на вершину?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        """
        фактически нужно посчитать n-нное число Фибоначчи,
        но в этой задаче первые два числа ряда равны 1 и 2, 
        потому что на 1-ую ступеньку мы можем подняться одним способом,
        а на вторую ступеньку можем подняться двумя способами:
        (2 шага по 1 ступеньке и 1 шаг по 2 ступеньки)
        """
        first, second = 1, 2

        for i in range(3, n + 1):
            cur = first + second
            first = second
            second = cur

        return second

tests_data = (
    (2, 2),
    (3, 3),
    (1, 1)

)
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.climbStairs(*data[:-1])
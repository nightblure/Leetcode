# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
            
        a, b = 1, 1

        for _ in range(2, n):
            next = a + b
            a, b = b, next

        return b

tests_data = {
    (2, 1), 
    (4, 3)
}
obj = Solution()

for data in tests_data:
    assert data[-1] == obj.fib(data[0])
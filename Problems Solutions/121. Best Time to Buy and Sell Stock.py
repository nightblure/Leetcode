# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices) -> int:
        
        """
        на каждой итерации выбираем минимальную цену покупки и после считаем максимальный профит
        """

        max_profit = 0 
        min_buy = prices[0]

        for price in prices[1:]:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)

        return max_profit

tests_data = (
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),

)
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.maxProfit(*data[:-1])
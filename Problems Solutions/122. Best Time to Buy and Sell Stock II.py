# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        
        """
        как только видим, что цена продажи (текущая цена) > цены покупки (предыдущая цена), продаем и накапливаем профит
        """

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

tests_data = (
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0)
)
obj = Solution()

for data in tests_data:
    expected = data[1]
    assert expected == obj.maxProfit(*data[:-1])
# https://leetcode.com/problems/moving-average-from-data-stream/description/

"""
Given a stream of integers and a window size, 
calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:
    * MovingAverage(int size) Initializes the object with the size of the window size.

    * double next(int val) Returns the moving average of the last size values of the stream.

"""

from collections import deque
from utils import display_func_value

class MovingAverage:

    def __init__(self, size: int):
        self.current_ma_value = 0
        self.data = deque()
        self.size = size

    @display_func_value
    def next(self, val: int) -> float:
        self.data.appendleft(val)
        self.current_ma_value += val

        # достигли размера окна (size) => нужно удалить самый первый элемент очереди
        if len(self.data) > self.size:
            self.current_ma_value -= self.data.pop()

        return self.current_ma_value / min(len(self.data), self.size)

movingAverage = MovingAverage(3)
movingAverage.next(1)  # return 1.0 = 1 / 1
movingAverage.next(10) # return 5.5 = (1 + 10) / 2
movingAverage.next(3)  # return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5)  # return 6.0 = (10 + 3 + 5) / 3
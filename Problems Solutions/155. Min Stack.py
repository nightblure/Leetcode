# https://leetcode.com/problems/min-stack/
from utils import display_func_value

class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    @display_func_value
    def top(self) -> int:
        return self.stack[-1]
    
    @display_func_value
    def getMin(self) -> int:
        return self.mins[-1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top()    # return 0
minStack.getMin() # return -2
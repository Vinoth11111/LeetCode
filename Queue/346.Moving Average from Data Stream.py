# premium problem
"""Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream."""
from collections import deque


class window_size:
    def __init__(self, size):
        self.size = size
        self.cnt = 0
        self.val = deque()

    def next(self, val: int) -> float:
        self.val.append(val)
        self.cnt += 1
        if self.cnt > self.size:
            self.val.popleft()
            self.cnt -= 1
        return sum(self.val)/self.cnt


obj = window_size(3)
print([obj.next(i) for i in [1, 10, 3, 5]])

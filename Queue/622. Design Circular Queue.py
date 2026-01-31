# https://leetcode.com/problems/design-circular-queue/description/

from collections import deque


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.qe = deque()
        self.re = 0

    def enQueue(self, value: int) -> bool:
        if len(self.qe) < self.k:
            self.qe.append(value)
            self.re = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.qe:
            self.qe.popleft()
            return True
        else:
            return False

    def Front(self) -> int:
        if self.qe:
            return self.qe[0]
        return -1

    def Rear(self) -> int:
        if self.qe:
            return self.re
        return -1

    def isEmpty(self) -> bool:
        return False if self.qe else True

    def isFull(self) -> bool:
        return len(self.qe) == self.k

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)

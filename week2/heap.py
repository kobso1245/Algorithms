from heapq import heappop, heappush, heappushpop

class Reversed:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

class MaxHeap:
    def __init__(self, k):
        self.max_heap = []
        self.volume = k

    def insert(self, value):
        if self.volume > 0:
            heappush(self.max_heap, Reversed(value))
            self.volume -= 1
        else:
            if value >= self.max_heap[0].value:
                return
            heappushpop(self.max_heap, Reversed(value))
    def get_kth(self):
        return self.max_heap[0].value



from heapq import heappush, heappop

class InvertedHeap:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False


    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Median:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.median = None
        self.min_heap_cnt = 0
        self.max_heap_cnt = 0

    def insert(self, elem):
        if self.max_heap == [] and self.min_heap == []:
            self.median = elem
            heappush(self.max_heap, InvertedHeap(elem))
            self.max_heap_cnt += 1
        else:
            if elem > self.median:
                heappush(self.min_heap, elem)
                self.min_heap_cnt += 1
            else:
                heappush(self.max_heap, InvertedHeap(elem))
                self.max_heap_cnt += 1
            if self.min_heap_cnt - self.max_heap_cnt in [0, 1]:
                self.median = self.min_heap[0]
            elif self.min_heap_cnt - self.max_heap_cnt == 2:
                elem_top = heappop(self.min_heap)
                self.min_heap_cnt -= 1
                heappush(self.max_heap, InvertedHeap(elem_top))
                self.max_heap_cnt += 1
                self.median = self.min_heap[0]
            elif self.min_heap_cnt - self.max_heap_cnt == -1:
                self.median = self.max_heap[0].value
            elif self.min_heap_cnt - self.max_heap_cnt == -2:
                elem_top = heappop(self.max_heap)
                self.max_heap_cnt -= 1
                heappush(self.min_heap, elem_top.value)
                self.min_heap_cnt += 1
                self.median = self.min_heap[0]
        return self.median

def test():
    med = Median()
    inp = input()
    elems = input().split(' ')
    arr = [int(x) for x in elems]
    for elem in arr:
        print(med.insert(elem))


test()

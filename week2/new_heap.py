import random
from heapq import heappush, heappop, heapify


def swap(first, second):
    k = first
    first = second
    second = k
    return first, second


def highest(curr, left, right):
    max_el = max(left, right)
    if curr < max_el:
        if left >= right:
            return 'left'
        else:
            return 'right'
    else:
        return 'curr'


class Heap:

    def __init__(self):
        self.max_heap = []
        self.last_pos = -1

    def insert(self, elem):
        self.max_heap.append(elem)
        self.last_pos += 1
        parrent_elem = (self.last_pos - 1) // 2
        curr_pos = self.last_pos

        while parrent_elem >= 0:
            if self.max_heap[parrent_elem] < self.max_heap[curr_pos]:
                self.max_heap[parrent_elem], self.max_heap[curr_pos] = swap(
                    self.max_heap[parrent_elem], self.max_heap[curr_pos])
            curr_pos = parrent_elem
            parrent_elem = (curr_pos - 1) // 2

    def __rev_heap(self, start_pos):
        curr_pos = start_pos
        left_pos = 2 * curr_pos + 1
        right_pos = 2 * curr_pos + 2

        while True:
            if left_pos <= self.last_pos:
                if right_pos <= self.last_pos:
                    subtree = highest(self.max_heap[curr_pos],
                                      self.max_heap[left_pos],
                                      self.max_heap[right_pos])
                    if subtree == 'curr':
                        break
                    elif subtree == 'left':
                        self.max_heap[curr_pos], self.max_heap[left_pos] = swap(
                            self.max_heap[curr_pos], self.max_heap[left_pos])
                        curr_pos = left_pos
                        left_pos = 2 * curr_pos + 1
                        right_pos = 2 * curr_pos + 2

                    else:
                        self.max_heap[curr_pos], self.max_heap[right_pos] = swap(
                            self.max_heap[curr_pos], self.max_heap[right_pos])
                        curr_pos = right_pos
                        left_pos = 2 * curr_pos + 1
                        right_pos = 2 * curr_pos + 2

                else:
                    if self.max_heap[curr_pos] < self.max_heap[left_pos]:
                        self.max_heap[curr_pos], self.max_heap[left_pos] = swap(
                            self.max_heap[curr_pos], self.max_heap[left_pos])
                        break
                    else:
                        break

            else:

                break
        return

    def pop(self):
        max_el = self.max_heap[0]
        self.max_heap[0], self.max_heap[self.last_pos] = swap(
            self.max_heap[0], self.max_heap[self.last_pos])
        self.last_pos -= 1
        self.max_heap = self.max_heap[:-1]
        self.__rev_heap(0)
        return max_el

    def __str__(self):
        return str(self.max_heap)

    def heapify(self):
        curr_pos = (self.last_pos - 1) // 2
        for i in range(curr_pos, -1, -1):
            self.__rev_heap(i)


def heap_sort(arr):
    hp = Heap()
    hp.max_heap = arr
    hp.last_pos = len(arr) - 1
    hp.heapify()

    res = []
    for i in range(len(arr)):
        res.append(hp.pop())

    return res[::-1]


def for_testing_heap_sort(arr):
    res = []
    length = len(arr)
    # heapify(arr)
    #hp = Heap()
    #hp.max_heap = arr
    #hp.last_pos = len(arr) - 1
    # hp.heapify()

    for i in range(length):
        res.append(heappop(arr))

    return res


def test():
    length = input()
    inp = input().split(' ')
    arr = [int(x) for x in inp]

    res = for_testing_heap_sort(arr)
    res = [str(x) for x in res]
    print(" ".join(res))

test()

class RMQ:
    def __init__(self, arr, length):
        self.arr = []
        self.length = 0
        self.__builder(arr, 0, length - 1, 0)
        self.orig_arr = arr
        self.arr_len = length

    def __builder(self, arr, start_index, end_index, pos):
        if end_index - start_index <= 1:
            if self.length - 1< pos:
                for i in range(self.length, pos + 1):
                    self.arr.append(0)
                    self.length += 1
            self.arr[pos]= (min(arr[start_index], arr[end_index]), (start_index, end_index))
            return self.arr[pos][0]
        self.arr[pos] = (min(self.__builder(arr, start_index, (start_index + end_index) // 2, 2*pos + 1),
                            self.__builder(arr, (start_index + end_index)//2 + 1, end_index,2*pos + 2)),
                            (start_index, end_index))
        return self.arr[pos][0]
    def __get(self, start, end, curr_start, curr_end, pos):

        if end < curr_start or start > curr_end:
            return 2 * 64

        if start <= curr_start and end >= curr_end:
            return self.arr[pos][0]

        if curr_end - curr_start == 1:
            if curr_end == start or curr_end == end:
                return self.orig_arr[curr_end]
            if curr_start == start or curr_start == end:
                return self.orig_arr[curr_start]
        if curr_start == curr_end and curr_start == start:
            return self.orig_arr[curr_start]

        left = self.__get(start, end, curr_start, (curr_end + curr_start)//2, 2*pos + 1)
        right = self.__get(start, end, (curr_end + curr_start)//2 + 1, curr_end, 2*pos + 2)
        
        return min(left, right) 

    def get(self,start, end):
        return self.__get(start, end, 0, self.arr_len - 1, 0)

    def add(self, index, value):
        self.__add(index, value, 0, 0, self.arr_len - 1)
        self.orig_arr[index] = value


    def __add(self, index, value, pos, curr_start, curr_end):
        if (curr_end - curr_start == 1 and (curr_end == index or curr_start == index)) or (curr_end == curr_start and index == curr_end):
            self.arr[pos] = (min(value, self.arr[pos][0]),
                            (curr_start, curr_end))
            return self.arr[pos][0]


        left_node_end = (curr_end + curr_start)//2
        right_node_start = (curr_end + curr_start) // 2 + 1
        if index <= left_node_end:
            self.arr[pos] = (min( self.__add(index, value, 2*pos + 1, curr_start, left_node_end),
                             self.arr[pos][0]),
                             (curr_start, curr_end))
        if index >= right_node_start:
            self.arr[pos] = (min(self.__add(index, value, 2*pos + 2, right_node_start, curr_end),
                             self.arr[pos][0]),
                             (curr_start, curr_end))
        return self.arr[pos][0]
        

def main():
    K = int(input().split(' ')[1])
    arrs = input().split(' ')
    rmq = RMQ([int(x) for x in arrs],len(arrs))
    res = []

    for i in range(K):
        inp = input().split(' ')
        if inp[0] == 'set':
            rmq.add(int(inp[1]), int(inp[2]))
        if inp[0] == 'min':
            res.append(rmq.get(int(inp[1]), int(inp[2])))
    while res != []:
        print(res.pop(0))
main()

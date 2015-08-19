class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = ""
        self.right_node = ""
        self.left_node_elems = 0
        self.right_node_elems = 0

class BST:
    def __init__(self):
        self.root = ""

    def insert(self, value):
        if self.root == "":
            self.root = Node(value)
            return True
        else:
            curr_node = self.root
            while True:
                if value > curr_node.value:
                    #otivame vdqsno
                    if curr_node.right_node != "":
                        curr_node.right_node_elems += 1
                        curr_node = curr_node.right_node
                    else:
                        curr_node.right_node_elems += 1
                        curr_node.right_node = Node(value)
                        return True
                elif value < curr_node.value:
                    curr_node.left_node_elems += 1
                    if curr_node.left_node != "":
                        curr_node = curr_node.left_node
                    else:
                        curr_node.left_node = Node(value)
                        return True

                else:
                    return False
                    
            return True

    def search(self, value):
        if self.root == "":
            return -1
        curr_node = self.root
        while True:
            if curr_node.value == value:
                return curr_node.right_node_elems
            if value > curr_node.value:
                curr_node = curr_node.right_node
            else:
                curr_node = curr_node.left_node

    def plot(self):
        que = []
        que.append(self.root)
        while len(que) != 0:
            curr_node = que.pop(0)
            print(curr_node.value, curr_node.left_node_elems, curr_node.right_node_elems)
            if curr_node.left_node != "":
                que.append(curr_node.left_node)
            if curr_node.right_node != "":
                que.append(curr_node.right_node)






def soldiers(num_rows, num_elems, arr):
    cnts = []
    tmp_cnt = 0
    lst_num = 1
    all_elems = []
    for lst in arr:
        tmp_cnt = 0
        bst = BST()
        elems = lst[::-1]
        for elem in elems:
            bst.insert(elem)
        
        #bst.plot()

        for elem in elems:
            res = bst.search(elem)
            #print(elem, res)
            
            if res != -1:
                tmp_cnt += res
        all_elems.append(tmp_cnt)
        cnts.append((lst_num, tmp_cnt))
        lst_num += 1
   
    #print(cnts) 
    max_ele = max(all_elems)
    for elem in cnts:
        if elem[1] == max_ele:
            return elem[0]

    
 
if __name__ == "__main__":
    unconv = input()
    tst = unconv.split(" ")
    N = int(tst[0])
    K = int(tst[1])
    
    arr =[]
    tmp_arr = []
    for x in range(K):
        tmp_arr = []
        tmp = input()
        unconv = tmp.split(" ")
        arr.append([int(elem) for elem in unconv])
    print(soldiers(K,N, arr))

 
    
    
    

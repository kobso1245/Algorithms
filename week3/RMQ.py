class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.left_node = None
        self.right_node = None



class BinarySearchHeap:
    def __init__(self):
        self.root = None

    def insert(self, value, index):
        if self.root:
            curr_node = self.root
            parrent_node = None
            is_right = False
            while curr_node:
                if curr_node.value == self.root.value and curr_node.index == self.root.index:
                    if curr_node.value > value:
                        previous_root = self.root
                        self.root = Node(value, index)
                        self.root.left_node = previous_root
                        return

                if curr_node.index < index:
                    #go right
                    if curr_node.right_node:
                        if curr_node.right_node.value <= value:
                            parrent_node = curr_node
                            curr_node = curr_node.right_node
                            is_right = True
                        else:
                            curr_right_child = curr_node.right_node
                            curr_node.right_node = Node(value, index)
                            curr_node.right_node.left_node = curr_right_child
                            return
                    else:
                        if curr_node.value <= value:
                            curr_node.right_node = Node(value, index)
                            return

                        else:
                            previous_curr_node = curr_node
                            if parrent_node:
                                if is_right:
                                    parrent_node.right_node = Node(value, index)
                                    parrent_node.right_node.left_node = previous_curr_node
                                    return
                                else:
                                    parrent_node.left_node = Node(value, index)
                                    parrent_node.left_node.left_node = previous_curr_node
                                    return
                            else:
                                self.root = Node(value, index)
                                self.root.left_node = previous_curr_node
                                return
                else:
                    #go left
                    if curr_node.left_node:
                        if curr_node.left_node.value <= value:
                            parrent_node = curr_node
                            curr_node = curr_node.left_node
                            is_right = False
                        else:
                            curr_left_child= curr_node.left_node
                            curr_node.left_node = Node(value, index)
                            curr_node.left_node.left_node = curr_left_child
                            return
                    else:
                        if curr_node.value <= value:
                            curr_node.left_node = Node(value, index)
                            return

                        else:
                            previous_curr_node = curr_node
                            if parrent_node:
                                if is_right:
                                    parrent_node.right_node = Node(value, index)
                                    parrent_node.right_node.left_node = previous_curr_node
                                    return
                                else:
                                    parrent_node.left_node = Node(value, index)
                                    parrent_node.left_node.left_node = previous_curr_node
                                    return
                            else:
                                self.root = Node(value, index)
                                self.root.right_node = previous_curr_node
                                return

        else:
            self.root = Node(value, index)


    def min_el(self, start, end):
        curr_node = self.root
        while curr_node:
            if curr_node.index < start:
                if curr_node.right_node:
                    curr_node = curr_node.right_node
                else:
                    return False
            elif curr_node.index > end:
                if curr_node.left_node:
                    curr_node = curr_node.left_node
                else:
                    return False
            else:
                return curr_node.value



    def set_el(self, index, value):
        curr_node = self.root
        parrent_node = None
        is_right = False


        while curr_node:
            if curr_node.index == index:
                #item found
                if curr_node.left_node and curr_node.right_node:
                    if parrent_node:
                        if parrent_node.value <= value and curr_node.left_node.value >= value and curr_node.right_node.value >= value:
                            curr_node.value = value
                            return
                        elif parrent_node.value > value and curr_node.left_node.value >= value and curr_node.right_node.value >= value:
                            pass

            elif curr_node.index < index:
                is_right = True
                parrent_node = curr_node
                curr_node = curr_node.right_node

            else:
                is_right = Flase
                parrent_node = curr_node
                curr_node = curr_node.left_node

    def set_elem(self, index, value):
        self.insert(value, index)


    def remove_el(self, index):
        curr_node = self.root
        parrent_node = None
        is_right = False
        while curr_node:
            if curr_node.index == index:
                # element found
                if curr_node.left_node and curr_node.right_node:
                    pass



                elif curr_node.left_node:
                    if parrent_node:
                        if is_right:
                            parrent_node.right_node = curr_node.left_node
                            return
                        else:
                            parrent_node.left_node = curr_node.left_node
                            return
                    else:
                        self.root = curr_node.left_node
                elif curr_node.right_node:
                    if parrent_node:
                        if is_right:
                            parrent_node.right_node = curr_node.right_node
                            return
                        else:
                            parrent_node.left_node = curr_node.right_node
                            return
                    else:
                        self.root = curr_node.right_node

                else:
                    if parrent_node:
                        if is_right:
                            parrent_node.right_node = None
                            return
                        else:
                            parrent_node.left_node = None
                            return
                    else:
                        self.root = None

            elif curr_node.index < index:
                is_right = True
                parrent_node = curr_node
                curr_node = curr_node.right_node

            else:
                is_right = False
                parrent_node = curr_node
                curr_node = curr_node.left_node


def test():
    inp = input().split(' ')
    elems = input().split(' ')
    arr = [int(x) for x in elems]
    srt = BinarySearchHeap()
    for i in range(len(arr)):
        srt.insert(arr[i], i)

    for i in range(int(inp[1])):
        inp_e = input().split(' ')
        if inp_e[0] == 'min':
            print(srt.min_el(int(inp_e[1]), int(inp_e[2])))
        else:
            srt.set_elem(int(inp_e[1]), int(inp_e[2]))
test()


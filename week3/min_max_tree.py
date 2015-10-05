class Node:

    def __init__(self, value=""):
        self.value = value
        self.left = ""
        self.right = ""


class BST:

    def __init__(self):
        self.root = Node()


class MinMaxHeap:

    def __init__(self):
        pass

    def isMinMax(self, root):
        que = []
        que.append((root, 1))

        while len(que) != 0:
            curr_node, level = que.pop(0)
            if level % 2 == 1:
                if curr_node.left != "" and curr_node.right != "":
                    if curr_node.left.value > curr_node.value and curr_node.right.value > curr_node.value:
                        que.append((curr_node.left, level + 1))
                        que.append((curr_node.right, level + 1))
                    else:
                        return False
                elif curr_node.left != "":
                    if curr_node.left.value > curr_node.value:
                        que.append((curr_node.left, level + 1))
                    else:
                        return False
                elif curr_node.right != "":
                    if curr_node.right.value > curr_node.value:
                        que.append((curr_node.right, level + 1))
                    else:
                        return False
                else:
                    pass
            else:
                if curr_node.left != "" and curr_node.right != "":
                    if curr_node.left.value < curr_node.value and curr_node.right.value < curr_node.value:
                        que.append((curr_node.left, level + 1))
                        que.append((curr_node.right, level + 1))
                    else:
                        return False
                elif curr_node.left != "":
                    if curr_node.left.value < curr_node.value:
                        que.append((curr_node.left, level + 1))
                    else:
                        return False
                elif curr_node.right != "":
                    if curr_node.right.value < curr_node.value:
                        que.append((curr_node.right, level + 1))
                    else:
                        return False
                else:
                    pass
        return True


a = BST()
b = MinMaxHeap()

a.root = Node(8)
a.root.left = Node(71)
a.root.right = Node(41)
a.root.left.left = Node(31)
a.root.left.right = Node(10)
a.root.right.left = Node(11)
a.root.right.right = Node(16)
a.root.left.left.left = Node(46)
a.root.left.left.right = Node(51)
a.root.left.right.left = Node(31)
a.root.left.right.right = Node(5)

print(b.isMinMax(a.root))

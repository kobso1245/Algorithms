class Node:
    def __init__(self, heapValue, treeValue):
        self.heapValue = heapValue
        self.treeValue = treeValue
        self.left = []
        self.right = []


def create_weird_tree(lst):
    if len(lst) == 0:
        return null

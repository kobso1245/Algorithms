class Node:
    def __init__(self, number="", name=""):
        self.number = number
        self.name = name
        self.left = ""
        self.right = ""
 
class PhoneBook:
    def __init__(self):
        self.root = Node()
        self.nodes_cnt = 0
        self.node_max_width = 0

    def insert(self, number, name):
        self.nodes_cnt += 1
        self.node_max_width = max(self.node_max_width, len(name))
        curr_node = self.root
        if curr_node.number == "":
            curr_node.number = number
            curr_node.name = name
            return
        while True:
            if name == curr_node.name:
                curr_node.number = number
                self.nodes_cnt -= 1
                return
            if name < curr_node.name:
                if curr_node.left != "":
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(number, name)
                    return
            else:
                if curr_node.right != "":
                    curr_node = curr_node.right
                else:
                    curr_node.right = Node(number, name)
                    return

    def list(self):
        curr_node = self.root
        que = []
        que.append(curr_node)
        while len(que) != 0:
            curr_node = que.pop(0)
            print("{} {}".format(curr_node.name, curr_node.number))
            if curr_node.left != "":
                que.append(curr_node.left)
            if curr_node.right != "":
                que.append(curr_node.right)

        return 

    def lookup(self, name):
        curr_node = self.root
        while True:
            if name == curr_node.name:
                return curr_node.number
            if name <= curr_node.name:
                if curr_node.left == "":
                    return "Name not found!"
                else:
                    curr_node = curr_node.left

            else:
                if curr_node.right == "":
                    return "Name not found!"
                else:
                    curr_node = curr_node.right

    def remove(self, name):
        curr_node = self.root
        parrent_node = ""
        parrent_left = ""
        while True:
            if curr_node.name == name:
                break
            if curr_node.name < name:
                if curr_node.right != "":
                    parrent_node = curr_node
                    curr_node = curr_node.right
                    parrent_left = False
                else:
                    return "Elem not found!"

            else:
                if curr_node.left !="":
                    parrent_node = curr_node
                    curr_node = curr_node.left
                    parrent_left = True
        result = self.__get_changing_elem(curr_node, parrent_node, parrent_left)
        if type(result) is not Node:
            return
        curr_node.name = result.name
        curr_node.number = result.number
        return  


    def __get_changing_elem(self, curr_node, parrent_node, parrent_left):
        last_value = 0
        parrent = ""
        if curr_node.name == self.root.name:
            if curr_node.left != "" and curr_node.right == "":
                self.root = curr_node.left
                return
            if curr_node.left == "" and curr_node.right == "":
                self.root = curr_node.right
                return

        if curr_node.left != "":
            if curr_node.left.right != "":
                curr_node = curr_node.left.right
                while curr_node.right!= "":
                    parrent = curr_node
                    curr_node = curr_node.right
                print(curr_node.name)

                if curr_node.left != "":
                    parrent.right = curr_node.left
                    return curr_node
                else:
                    parrent.right = ""
                    return curr_node

        if curr_node.right != "":
            if curr_node.right.left != "":
                curr_node = curr_node.right.left
                while curr_node.left != "":
                    parrent = curr_node
                    curr_node = curr_node.left

                if curr_node.right != "":
                    parrent.right = curr_node.right
                    return curr_node
                
        else:
            if parrent_node == "":
                curr_node = ""
                return
            if parrent_left:
                parrent_node.left = ""
            else:
                parrent_node.right = ""



a = PhoneBook()
a.insert(1, "Stanislav")
a.insert(2, "Qvor")
a.insert(15, "Rado")
a.insert(-1, "Ivo")
print(a.lookup("Rado"))
a.insert(6, "Ivan")
print(a.lookup("Ivan"))
a.insert(8, "Ivan")
print(a.lookup("Ivan"))
print(a.lookup("Pesho"))
a.insert(23, "Ani")
a.insert(44, "Pesho")
a.insert(77, "Eli")
a.insert(83, "Georgi")
a.list()
print(a.remove("Stanislav"))
print()
a.list()

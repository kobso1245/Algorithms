import json

class Node:
    def __init__(self):
        self.ends_word = False
        self.children = dict()

    def __repr__(self):
        return str(self.children)
    def __str__(self):
        return str(self.children)

class WordDict:
    def __init__(self):
        self.root = None
 
    def insert(self, word):
        if self.root == None:
            self.root = Node()
            curr_node = self.root
            for letter in word:
                curr_node.children[letter] = Node()
                curr_node = curr_node.children[letter]
            curr_node.ends_word = True
            return
        curr_node = self.root
        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                curr_node.children[letter] = Node()
                curr_node = curr_node.children[letter]
        curr_node.ends_word = True
        return 


    def lookup(self, word):
        curr_node = self.root
        if not curr_node:
            return False
        for letter in word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                return False

        if curr_node.ends_word:
            return True
        else:
            return False

    def __str__(self):
        return str(self.root)

def tester():
    result = []
    wrd = WordDict()
    rows = int(input())
    for i in range(rows):
        command = input()
        actual_command = command.split(' ')[0]
        argument = command.split(' ')[1]
        if actual_command == 'insert':
            try:
                wrd.insert(argument)
            except Exception:
                result.append('false')
        elif actual_command == 'contains':
            result.append(wrd.lookup(argument))
        else:
            pass

    for word in result:
        if word:
            print('true')
        else:
            print('false')


tester()

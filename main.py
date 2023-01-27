class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


nodeOne = Node('Sadam')
nodeTwo = Node('Hamza')
nodeThree = Node('Asad')


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        pass


linKedList = LinkedList()
linKedList.insert(nodeOne)
linKedList.insert(nodeTwo)
linKedList.insert(nodeThree)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None

    # sadam - > none
    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                break
            current_node = current_node.next
            new_node.previous = current_node


nodeOne = Node('Sadam')
nodeTwo = Node('Hamza')
nodeThree = Node('Asad')

linKedList = LinkedList()
linKedList.insert(nodeOne)
linKedList.insert(nodeTwo)
linKedList.insert(nodeThree)

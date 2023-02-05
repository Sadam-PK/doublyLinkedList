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
        current_node.next = new_node
        new_node.previous = current_node

    def print(self):
        if self.head is None:
            print('list is empty!')
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next

    def reverse(self):
        if self.head is None:
            print('List empty..')
            return
        current_node = self.head
        reverse_node = None
        while True:
            if current_node is None:
                break
            if current_node.next is None:
                reverse_node = current_node
            current_node = current_node.next
            while True:
                if reverse_node is None:
                    break
                print(reverse_node.data)
                reverse_node = reverse_node.previous

    def insert_at_head(self, new_node):
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        temp_node.previous = self.head

    def insert_at(self, new_node, position):
        current_node = self.head
        current_position = 0
        while True:
            if current_position == position:
                current_node.previous.next = new_node
                new_node.next = current_node
                new_node.previous = current_node.previous
                current_node.previous = new_node
                break
            current_node = current_node.next
            current_position += 1

    # sadam <-> ahad -> hamza <-> asad


nodeOne = Node('Sadam')
nodeTwo = Node('Hamza')
nodeThree = Node('Asad')

linKedList = LinkedList()
linKedList.insert(nodeOne)
linKedList.insert(nodeTwo)
linKedList.insert(nodeThree)
# linKedList.print()
# linKedList.reverse()
nodeFour = Node('Ahad')
# linKedList.insert_at_head(nodeFour)
linKedList.insert_at(nodeFour, 1)
linKedList.print()

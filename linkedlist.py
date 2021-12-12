class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.append(5)
ll.append(7)
ll.append(2)
ll.append(3)
ll.append(6)
ll.printList()
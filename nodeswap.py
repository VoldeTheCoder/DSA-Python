class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def swap(self, k):
        tmp = self.head
        total = 0
        while tmp:
            total +=1
            tmp = tmp.next
        first, second = k, total-k+1
        if self.head.next is None or (total//2 + 1 == first and total%2 !=0 ): 
            return self.head
        current = self.head
        count = 0
        while current:
            count += 1
            if count == first - 1:
                lpnode = current
            if count == first:
                lnode = current
            if count == second - 1:
                rpnode = current
            if count == second:
                rnode = current
            current = current.next
        if total == 2:
            temp = self.head
            self.head = self.head.next
            self.head.next = temp
            temp.next = None
        else:
            if first == 1:
                temp = self.head
                rnode.next = self.head.next
                self.head = rnode
                rpnode.next = temp
                temp.next = None
            elif first == total:
                temp = self.head
                lnode.next = self.head.next
                self.head = lnode
                lpnode.next = temp
                temp.next = None
            elif second-first == 1:
                lnode.next = rnode.next
                rnode.next = lnode
                lpnode.next = rnode
            elif first-second == 1:
                rnode.next = lnode.next
                lnode.next = rnode
                rpnode.next = lnode
            else:
                tmp3 = lnode.next
                lnode.next = rnode.next
                rnode.next = tmp3
                lpnode.next = rnode
                rpnode.next = lnode

    
ll = LinkedList()

ll.append(10)
ll.append(4)
ll.append(6)
ll.append(9)
ll.append(13)
ll.append(2)
ll.append(23)
ll.append(15)

ll.swap(5)
ll.printList()


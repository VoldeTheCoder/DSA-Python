import os
import sys


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
    
    def swapNodes(self):
        os.system('cls')
        if self.head is None:
            input("List is empty.. ")
            commandInterface(self)
        self.printList(4)
        node_pos = int(input("Enter node postion to swap: "))
        tmp = self.head
        total = 0
        while tmp:
            total +=1
            tmp = tmp.next
        if node_pos < 1 or node_pos > total:
            input("Postion not in List!")
            self.swapNodes()
        else:
            first, second = node_pos, total-node_pos+1
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
                print("Nodes swapped!!")
                self.printList(3)
                input("Press any key...")
                commandInterface(self)

    def deleteNode(self):
        os.system('cls')
        
        if self.head is None:
            print("List is already empty")
            input("Press any key...")
            commandInterface(self)
        self.printList(4)
        tmp = self.head
        val = int(input("Enter the element to be deleted: "))
        found = False
        while tmp and tmp.next:
            if tmp.data == val:
                found = True
                tmp.data = tmp.next.data
                tmp.next = tmp.next.next
            tmp = tmp.next
        if not found:
            print("Element", val, "not found in the List!")
            input("Press any key to continue...")
        else:
            print("Element found!")
            print("Deleted", val, "from the List...")
            self.printList(3)
            input("Press any key to continue...")
        commandInterface(self)
    
    def printList(self, check):
        if check == 0:
            os.system('cls')
        if self.head is None:
            print("List is currently empty")
        else:
            if check == 3:
                print("Updated List elements are-----------")
            else:
                print("List elements are---------")
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        if check == 0:
            input("Press any key to continue..")
            commandInterface(self)
        else:
            return

    def addNode(self):
        os.system('cls')
        add = True
        self.printList(1)
        try:
            opt = int(input("1. Push\n2. Append\n(1/2): "))
            if opt < 1 or opt > 2:
                print("Invalid choice!")
                input("Press any key...")
                self.addNode() 
            ans = True
            while ans is not False and add is True:
                val = int(input("Element : "))
                if opt == 2:
                    self.append(val)
                elif opt == 1:
                    self.push(val)
                more = str(input("More(y/n)? : "))
                if more == 'n' or more == 'y':
                    if more == 'n':
                        ans = False
            input("Elements added! \nPress any key to go back..")
            commandInterface(self)
        except:
            commandInterface(self)

    def action(self, opt):
        if opt == 1:
            self.addNode()
        elif opt == 2:
            self.printList(0)
        elif opt == 3:
            self.deleteNode()
        elif opt == 4:
            self.swapNodes()
        elif opt == 5:
            sys.exit()
        else:
            input("Invalid choice!")
            commandInterface(self)
        
def commandInterface(List):
    os.system('cls')
    print("Operations to perform....")
    print("1. Add a node")
    print("2. Print List")
    print("3. Delete a Node")
    print("4. Swap Nodes")
    print("5. Exit")
    choice = int(input("(1/2/3/4/5) : "))
    List.action(choice)   

commandInterface(LinkedList())
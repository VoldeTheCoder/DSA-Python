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

    def deleteNode(self):
        val = int(input("Enter the element to be deleted: "))
        found = False
        if self.head is None:
            print("List is already empty")
            return
        tmp = self.head
        
        while tmp and tmp.next:
            if tmp.data == val:
                found = True
                tmp.data = tmp.next.data
                tmp.next = tmp.next.next
            tmp = tmp.next
        if not found:
            print("Element", val, "not found in the List!")
        else:
            print("Element found!")
            print("Deleted", val, "from the List...")
        commandInterface(self)
    
    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            print("List elements are: ")
            while temp:
                print(temp.data)
                temp = temp.next
        input("Print Enter to go back to menu..")
        commandInterface(self)

    def createList(self):
        print("Enter element: ")
        ans = True
        while ans is not False:
            try:
                val = int(input())
                self.append(val)
                add = input("More(y/n)? : ")
                if add == 'n' or add == 'y':
                    if add == 'n':
                        ans = False
                else:
                    print("Wrong input entered!")
                    self.createList
            except ValueError:
                input("Entered value should be an integer..")
                self.createList()
        input("Elements added! \nPress any key to go back..")
        commandInterface(self)

    def action(self, opt):
        if opt == 1:
            self.createList()
        elif opt == 2:
            self.printList()
        elif opt == 3:
            self.deleteNode()
        elif opt == 4:
            return
        else:
            input("Invalid choice!")
            commandInterface(self)
        
def commandInterface(List):
    print("Operations to perform....")
    print("1. Create List")
    print("2. Print List")
    print("3. Delete a Node")
    print("4. Exit")
    choice = int(input("(1/2/3/4) : "))
    List.action(choice)   

commandInterface(LinkedList())
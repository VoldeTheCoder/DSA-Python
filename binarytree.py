class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data, node):
        new_node = TreeNode(data)
        if self.root:
            if data < node.data:
                if node.left:
                    self.insert(data, node.left)
                else:
                    node.left = new_node
                    print("A left node added!")
            elif data > node.data:
                if node.right:
                    self.insert(data, node.right)
                else:
                    node.right = new_node
                    print("A right node added!")
        else:
            self.root = new_node
            print("Root added!")
            
    def addNode(self):
        add_more = "y"
        while add_more != "n":
            data = int(input("Enter data to be added: "))
            self.insert(data, self.root)
            add_more = input("Wanna add more?(y/n): ")
            
    def depth(self, node):
        if node is None:
            return -1
        else:
            ldepth = self.depth(node.left)
            rdepth = self.depth(node.right)
            
            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
    def sumTree(self, node):
        if node.left is None:
            return node.data
        return node.data + self.sumTree(node.left) + self.sumTree(node.right)
    
    def printTree(self, node, height):
        print(node.data, end=" ")
        if node.left:
            self.printTree(node.left, height-1)
        if node.right:
            self.printTree(node.right, height+1)

bit = BinaryTree()
bit.addNode()
bit.printTree(bit.root, bit.depth(bit.root))
print(bit.sumTree(bit.root))
         
#Binary search tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.rec(self.root,data)

    def rec(self,node,data):
        if data>node.data:
            if node.right is None:
                node.right=Node(data)
            else:
                self.rec(node.right,data)
        else:
            if node.left is None:
                node.left=Node(data)
            else:
                self.rec(node.left,data)

    def inorder(self,node):
        if not node:
            return
        
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)

    def preorder(self,node):
        if not node:
            return
        
        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self,node):
        if not node:
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")

bst=BST()
values=[5,7,3,4,9,6,1]
for v in values:
    bst.insert(v)
bst.inorder(bst.root)
print()
bst.preorder(bst.root)
print()
bst.postorder(bst.root)
print()

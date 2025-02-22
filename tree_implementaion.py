class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Changed from Left to left
        self.right = None # Changed from Right to right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            self.insert_recursively(self.root, new_node)

    def insert_recursively(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_recursively(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_recursively(current_node.right, new_node)
    
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def print_inorder(self):
        self.inorder_traversal(self.root)  # Corrected method call
        print()  # Newline for better readability

# Example Usage:
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)

bt.print_inorder()

# === Arrays and Matrices ===

class DynamicArray:
    """A basic implementation of a dynamic array."""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        """Access element at a given index."""
        if not 0 <= index < len(self._data):
            raise IndexError('Invalid index')
        return self._data[index]

    def insert(self, index, value):
        """Insert value at a specific index."""
        if not 0 <= index <= len(self._data):
            raise IndexError('Invalid index')
        self._data.insert(index, value)

    def delete(self, index):
        """Delete element at a specific index."""
        if not 0 <= index < len(self._data):
            raise IndexError('Invalid index')
        del self._data[index]

    def __str__(self):
        return str(self._data)

# Matrix creation is straightforward using nested lists
def create_matrix(rows, cols, default_value=0):
    """Creates a 2D matrix (list of lists)."""
    return [[default_value for _ in range(cols)] for _ in range(rows)]

# === Stacks and Queues (using Arrays/Lists) ===

class ArrayStack:
    """LIFO Stack implementation using a Python list."""
    def __init__(self):
        self._data = []

    def push(self, value):
        """Add an element to the top of the stack."""
        self._data.append(value)

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self._data:
            raise IndexError('pop from an empty stack')
        return self._data.pop()

    def peek(self):
        """Return the top element without removing it."""
        if not self._data:
            raise IndexError('peek from an empty stack')
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

class ArrayQueue:
    """FIFO Queue implementation using a Python list."""
    def __init__(self):
        self._data = []

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self._data.append(value)

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if not self._data:
            raise IndexError('dequeue from an empty queue')
        return self._data.pop(0) # Inefficient operation

    def first(self):
        """Return the first element without removing it."""
        if not self._data:
            raise IndexError('first from an empty queue')
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

# === Linked Lists ===

class Node:
    """A node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Singly linked list implementation."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        """Deletes the first occurrence of a node with the given key."""
        current = self.head
        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        # If key was not present in linked list
        if not current:
            return
        # Unlink the node
        prev.next = current.next
        current = None

    def traverse(self):
        """Print all elements of the linked list."""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# === Optional: Rooted Trees ===

class TreeNode:
    """A node in a rooted tree."""
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        """Add a child node."""
        child_node.parent = self
        self.children.append(child_node)

class Tree:
    """A simple rooted tree."""
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def print_tree(self, node, level=0):
        """Prints the tree structure."""
        if node:
            print(' ' * level * 4 + '|-- ' + str(node.data))
            for child in node.children:
                self.print_tree(child, level + 1)
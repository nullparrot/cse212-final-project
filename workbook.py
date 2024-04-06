class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        self.s2 = self.s1[:]
        self.s1 = [value] + self.s2

    def dequeue(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def __iter__(self):
        while len(self.s1) > 0:
            yield self.s1.pop()

    def __reversed__(self):
        for z in self.s1:
            yield z

    def __str__(self):
        if len(self.s1) == 0:
            return 'Empty Queue'
        output = 'Queue{'
        first = True
        self.s2 = self.s1
        while len(self.s2) > 0:
            if first:
                first = False
            else:
                output += ', '
            output += str(self.s2.pop())
        output +='}'
        return output
    
    def __len__(self):
        return len(self.s1)
    
    def __getitem__(self, i):
        if i >= len(self.s1):
            raise IndexError(f'Error index "{i}" is out of range')
        altIndex = len(self.s1)-1-i
        return self.s1[altIndex]

class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self, value):
        new_node = LinkedList.Node(value)  
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, value):
        new_node = LinkedList.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next
            
    def remove_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_tail(new_value)
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next

    def remove(self, value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.remove_tail()
                elif curr == self.head:
                    self.remove_head()
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr = None
                return
            curr = curr.next
        pass

    def replace(self, old_value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            if curr == self.tail:
                return
            else:
                curr = curr.next
        pass

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        curr = self.tail
        while curr is not None:
            yield curr.data
            curr = curr.prev

    def __str__(self):
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

class BST:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    def __contains__(self, data):
        return self._contains(data, self.root)

    def _contains(self, data, node):
        if node.data is not None:
            if node.data == data:
                return True
            elif data < node.data and node.left is not None:
                return self._contains(data, node.left)
            elif data > node.data and node.right is not None:
                return self._contains(data, node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):    
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
        if node.right is not None:
            right = (self._get_height(node.right))+1
        else:
            right = 1
        if node.left is not None:
            left = (self._get_height(node.left))+1
        else:
            left = 1
        return max(right,left)

# NOTE: Functions below are not part of the BST class above. They can be used to create a BST form a sorted list

def create_bst_from_sorted_list(sorted_list):
    bst = BST()  # Create an empty BST to start with 
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

def _insert_middle(sorted_list, first, last, bst):
    if last == -1:
        pass
    elif last == first:
        bst.insert(sorted_list[first])
    elif last-first == 1:
        bst.insert(sorted_list[first])
        bst.insert(sorted_list[last])
    else:
        middle = int((first+last)/2)
        bst.insert(sorted_list[middle])
        _insert_middle(sorted_list,first,middle-1,bst)
        _insert_middle(sorted_list,middle+1,last,bst)
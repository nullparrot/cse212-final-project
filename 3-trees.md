# Trees

Trees are an ordered and sorted data structure. They're similar to a linked list in principle, but rather than a single chain of linked data, it branches. Starting at the first node, or the root, there are two linked nodes. This branching allows the data to be aranged in a way that searches can be performed very efficently. 


# Sample Tree Class

``` python
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
```
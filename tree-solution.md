[Return to Lesson](3-trees.md)

## Problem Example

Finding the path is effectivly the same as finding a value in the tree. The main difference is that we need to build a string that stores the path as we travel down the tree. We'll store the path in the 'pathway' variable.

```python
def find_path(self, data):
    pathway = ""
    node = self.root
    pathway = self._path(data, node, pathway)
    return pathway

def _path(self, data, node, pathway):
    if node.data is not None:
        if node.data == data:
            pathway = f'{pathway}{node.data}'
            print
            return pathway
        elif data < node.data and node.left is not None:
            pathway = f'{pathway}{node.data}-'
            return self._path(data, node.left, pathway)
        elif data > node.data and node.right is not None:
            pathway = f'{pathway}{node.data}-'
            return self._path(data, node.right, pathway)
```

## Complete Class Example

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

    def find_path(self, data):
        pathway = ""
        node = self.root
        pathway = self._path(data, node, pathway)
        return pathway
    
    def _path(self, data, node, pathway):
        if node.data is not None:
            if node.data == data:
                pathway = f'{pathway}{node.data}'
                print
                return pathway
            elif data < node.data and node.left is not None:
                pathway = f'{pathway}{node.data}-'
                return self._path(data, node.left, pathway)
            elif data > node.data and node.right is not None:
                pathway = f'{pathway}{node.data}-'
                return self._path(data, node.right, pathway)
```
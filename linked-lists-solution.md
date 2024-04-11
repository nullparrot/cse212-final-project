[Return to Lesson](2-linked-lists.md)

## Insert At Function Example

```python
def insert_at(self, index, value):
    if index == 0:
        self.insertHead(value)
    else:
        currNode = self.head
        currPos = 1
        while currPos != index and currNode != self.tail:
                currPos = currPos+1
                currNode = currNode.next
        if currNode == self.tail:
            self.insert_tail(value)
        else:
            new_node = LinkedList.Node(value)
            new_node.prev = currNode
            new_node.next = currNode.next
            currNode.next.prev = new_node
            currNode.next = new_node
```

## Complete Class

```python
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

    def insert_at(self, index, value):
        if index == 0:
            self.insertHead(value)
        else:
            currNode = self.head
            currPos = 1
            while currPos != index and currNode != self.tail:
                    currPos = currPos+1
                    currNode = currNode.next
            if currNode == self.tail:
                self.insert_tail(value)
            else:
                new_node = LinkedList.Node(value)
                new_node.prev = currNode
                new_node.next = currNode.next
                currNode.next.prev = new_node
                currNode.next = new_node

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

    def replace(self, old_value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            if curr == self.tail:
                return
            else:
                curr = curr.next

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
```
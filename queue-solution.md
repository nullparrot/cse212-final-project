[Return to Lesson](1-queues.md)

## Reverse Function Example

```python
def __reversed__(self):
    while len(self.s1) > 0:
        yield self.s1.pop(0)
```

## Complete Class

```python
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
        while len(self.s1) > 0:
            yield self.s1.pop(0)

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
```
from random import randint
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return (' -> '.join(values))
    
    def __len__(self):
        result = 0
        current_node = self.head
        while current_node:
            result += 1
            current_node = current_node.next
        return result
    
    def add(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node 
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self.tail

    def generate(self,n,min,max):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min,max))
        return self
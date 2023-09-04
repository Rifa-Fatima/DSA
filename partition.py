from sampleLL import LinkedList

def partition(ll,x):
    current_node = ll.head
    ll.tail = ll.head
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < x:
            current_node.next = ll.head
            ll.head = current_node
        else:
            ll.tail.next = current_node
            ll.tail = current_node
        current_node = next_node

    if ll.tail.next is not None:
        ll.tail.next = None
    

customLL = LinkedList()
customLL.generate(10,10,99)
print(customLL)
print(partition(customLL,56))
print(customLL)
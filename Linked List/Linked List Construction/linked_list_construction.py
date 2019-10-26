class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # if there is not tail set
        if self.tail is None:
            self.setHead(node)
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # one case might be that if nodeToInsert is head and the tail both then we return
        if nodeToInsert.head == self.head and nodeToInsert.tail == self.tail:
            return

        # here we are considering that the node can be present in the list itself and then we have to move it
        self.remove(nodeToInsert)
        # 1 <> 2 <> 3 <> 4 <> 5
        # remove 4 => < 4 >
        # current node < 2 >
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        # check if the element that we are inserting before the head of the ll
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # traverse through the nodes and keep the temporary variable
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        # removing a node considering the node is never given to be null to us
        # check if the node we are dealing with is the head
        # check if the node we are dealing is not tail
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        # there may be single node thus we may safely remove elif condition

        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        # 1 <> 2 <> 3 <> 4 <> 5
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        node = self.head

        while node is not None and node.value != value:
            node = node.next
        return node is not None


node = Node(1)
ll = DoublyLinkedList()
ll.setHead(node)
print(ll.tail.value)
for i in range(2, 6):
    _node = Node(i)
    ll.insertAfter(node, _node)
node = ll.head
while node is not None:
    print(node.value)
    node = node.next

ll.removeNodesWithValue(3)

print("-----")
node = ll.head
while node is not None:
    print(node.value)
    node = node.next

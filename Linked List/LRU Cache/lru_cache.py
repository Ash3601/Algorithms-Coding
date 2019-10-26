class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        node = self
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
        elif self.head == self.tail:  # only one node
            node.next = self.tail
            self.tail.prev = node
            self.head = node
        else:
            # if the node is the tail and if we have to move it to the top
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            # 4 <> 5 <> 6
            node.next = self.head
            self.head.prev = node
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev  # make prev node as the tail
        self.tail.next = None  # make the next node as None to delete it


class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.currentSize = 0
        self.listOfMostRecent = DoublyLL()
        self.maxSize = maxSize or 1

    def insertKeyValuePair(self, key, value):
        node = Node(key, value)
        if key not in self.cache.keys():
            if self.currentSize == self.maxSize:
                # We have to evict the most recent
                self.evictLeastRecent(node)
            else:
                self.currentSize += 1
            self.cache[key] = node
        else:
            # TODO
            self.replaceKey(key, value)
        self.updateMostRecent(node)

        # self.listOfMostRecent.setHeadTo(node)
    def replaceKey(self, key, newValue):
        nodeToUpdate = self.cache[key]
        nodeToUpdate.value = newValue

    def evictLeastRecent(self, node):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

    def getValueFromKey(self, key):
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        return self.listOfMostRecent.head.key

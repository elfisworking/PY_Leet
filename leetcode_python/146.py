class LinkNode:
    def __init__(self, key=0, value=0):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = LinkNode(0, 0)
        self.tail = LinkNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = LinkNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                print(removed.key)
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            print(node.value)
            node.value = value
            self.moveToHead(node)




    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
        



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 2)

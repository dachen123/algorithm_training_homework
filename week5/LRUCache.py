#146.LRU缓存机制
class doubleLinkNode:
    def __init__(self,key,val):
        self.val = val 
        self.key = key
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = doubleLinkNode(-1,-1)
        self.tail = doubleLinkNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head  
        self.capacity = capacity
        self.counter = 0
    
    def del_node(self,node):
        node.prev.next = node.next 
        node.next.prev = node.prev 
        return node 

    def add_node_to_head(self,node):
        node.next = self.head.next 
        self.head.next.prev = node 
        node.prev = self.head 
        self.head.next = node 

    def move_node_to_head(self,node):
        node = self.del_node(node)
        self.add_node_to_head(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_node_to_head(node)
            return node.val 
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = doubleLinkNode(key,value)
            self.cache[key] = node 
            self.add_node_to_head(node)
            if self.counter >= self.capacity:
                node = self.del_node(self.tail.prev)
                self.cache.pop(node.key)
            else:
                self.counter += 1
        else:
            node = self.cache[key]
            node.val = value
            self.move_node_to_head(node)
            
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
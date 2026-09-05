class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, node):
        # 1 -> 2 -> 3
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        # lru (dummy) -> 1 -> 2 -> 3 -> mru (dummy)
        prev = self.mru.prev
        nxt = self.mru
        
        prev.next = node
        node.prev = prev
        
        node.next = nxt
        nxt.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.cap:
                lru_node = self.lru.next
                self.remove(lru_node)
                del self.cache[lru_node.key]
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)

        

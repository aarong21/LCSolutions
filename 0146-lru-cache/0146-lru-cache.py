class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from left side of list
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    # insert to right side of list
    def insert(self, node):
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update LRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # create node
        self.insert(self.cache[key]) # add node to ll

        # if cache length longer than capacity
        if len(self.cache) > self.cap:
            rem = self.left.next
            self.remove(rem)
            del self.cache[rem.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
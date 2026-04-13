# No external libraries needed for this optimal approach

# ---- SOLUTION ----
# Represents a node in DLL
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

# Manages the cache operations
class LRUCache:
    def __init__(self, capacity: int):
        # step 1: store max size limit
        self.cap = capacity
        # step 2: map keys to nodes
        self.cache = {}
        # step 3: setup dummy head, tail
        self.left, self.right = Node(0, 0), Node(0, 0)
        # step 4: connect dummy nodes together
        self.left.next, self.right.prev = self.right, self.left

    # Helper: remove node from list
    def remove(self, node):
        # step 1: bypass the target node
        prev, nxt = node.prev, node.next
        # step 2: link neighbors to each-other
        prev.next, nxt.prev = nxt, prev

    # Helper: insert node at MRU
    def insert(self, node):
        # step 1: find spot before tail
        prev, nxt = self.right.prev, self.right
        # step 2: link previous to node
        prev.next = nxt.prev = node
        # step 3: link node to neighbors
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        # step 1: check if key exists
        if key in self.cache:
            # step 2: mark as recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # step 3: return the stored value
            return self.cache[key].val
        # step 4: return default missing value
        return -1

    def put(self, key: int, value: int) -> None:
        # step 1: remove existing old node
        if key in self.cache:
            self.remove(self.cache[key])
        
        # step 2: create and insert new
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # step 3: evict if over capacity
        if len(self.cache) > self.cap:
            # step 4: identify LRU at head
            lru = self.left.next
            # step 5: remove LRU from list
            self.remove(lru)
            # step 6: delete from hash map
            del self.cache[lru.key]

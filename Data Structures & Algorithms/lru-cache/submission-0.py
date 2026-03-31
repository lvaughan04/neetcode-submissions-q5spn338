class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.current = 0
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        ## to re
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def append(self, node):
        ## comes in before right so get rights previous node
        prev = self.right.prev
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        ## remove it from where it was
        self.remove(self.cache[key])
        ## add it to right before right node to make it most recently used
        self.append(self.cache[key]) 
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            ## if the key is in it, remove it and update it then add it
            self.remove(self.cache[key])
        node = ListNode(key,value)
        self.cache[key] = node
        self.append(node)
        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
            

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

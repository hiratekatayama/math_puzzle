from collections import deque, OrderedDict


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.dummy = ListNode("#")
        self.current = self.dummy

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.map[key][1]
            if node != self.current:
                self.deleteNode(node)
                self.insert(node)
            return self.map[key][0]
        return -1

    def deleteNode(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next, node.prev = None, None

    def insert(self, node):
        self.current = node
        node.prev = self.current
        self.current = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.size < self.capacity:
            if key not in self.map:
                node = ListNode(key)
                self.insert(node)
                self.map[key] = [value, node]
                self.size += 1
            else:
                node = self.map[key][1]
                if node != self.current:
                    self.deleteNode(node)
                    self.insert(node)
                self.map[key][0] = value
        else:
            if key in self.map:
                node = self.map[key][1]
                if node != self.current:
                    self.deleteNode(node)
                    self.insert(node)
                self.map[key][0] = value
            else:
                head = self.dummy.next
                self.deleteNode(head)
                del self.map[head.val]
                node = ListNode(key)
                self.insert(node)
                self.map[key] = [value, node]


class LRUCache2(object):
    def __init__(self, capacity):
        self.size = capacity
        self.deque = deque()

    def _find(self, key):
        for i in range(len(self.deque)):
            n = self.deque[i]
            if n[0] == key:
                return i
        return -1

    def get(self, key):
        idx = self._find(key)
        if idx == -1:
            return -1
        else:
            k, v = self.deque[idx]
            del self.deque[idx]
            self.deque.append((k, v))
            return v

    def put(self, key, value):
        idx = self._find(key)
        if idx == -1:
            if len(self.deque) >= self.size:
                self.deque.popleft()
            self.deque.append((key, value))
        else:
            del self.deque[idx]
            self.deque.append((key, value))

class LRUCache3(object):
    def __init__(self, capacity):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key)

        self.cache[key] = value

if __name__ == "__main__":
    #cache = LRUCache(2)
    #cache = LRUCache2(2)
    cache = LRUCache3(2)

    print(cache.put(1, 1))
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
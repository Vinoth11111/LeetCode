# https://leetcode.com/problems/lru-cache/description/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            self._remove_node(node)
            self._add_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            node.value = value
            self._remove_node(node)
            self._add_node(node)
        else:
            if len(self.lru) >= self.capacity:
                lru_node = self.tail.prev
                del self.lru[lru_node.key]
                self._remove_node(lru_node)
            new_node = Node(key, value)
            self.lru[key] = new_node
            self._add_node(new_node)

from threading import Lock
from typing import Any, Dict, Optional


class Node:
    """Node for the doubly linked list."""

    def __init__(self, key: Any = None, value: Any = None):
        self.key = key
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    """Thread-safe LRU Cache."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")

        self.capacity = capacity
        self.cache: Dict[Any, Node] = {}
        self.lock = Lock()

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node: Node) -> None:
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

    def get(self, key: Any):
        """Return value if present, otherwise -1."""

        with self.lock:
            if key not in self.cache:
                return -1

            node = self.cache[key]

            self._remove(node)
            self._insert(node)

            return node.value

    def put(self, key: Any, value: Any) -> None:
        """Insert or update a key."""

        with self.lock:

            if key in self.cache:
                node = self.cache[key]
                node.value = value

                self._remove(node)
                self._insert(node)
                return

            node = Node(key, value)

            self.cache[key] = node
            self._insert(node)

            if len(self.cache) > self.capacity:
                lru = self.tail.prev

                self._remove(lru)
                del self.cache[lru.key]

    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

    def display_cache(self):
        current = self.head.next

        print("\nCurrent Cache (MRU -> LRU)")

        while current != self.tail:
            print(f"{current.key} -> {current.value}")
            current = current.next
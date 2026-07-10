# Thread-Safe LRU Cache in Python

## Overview

This project is my implementation of a Thread-Safe Least Recently Used (LRU) Cache in Python. The main goal was to build a cache that supports fast `get()` and `put()` operations while allowing multiple threads to access it safely.

To achieve this, I used a combination of a dictionary and a doubly linked list. The dictionary provides quick access to cached items, while the doubly linked list keeps track of the order in which items are used. A `threading.Lock` is used to prevent multiple threads from modifying the cache at the same time.

---

## Project Structure

```
thread_safe_lru_cache/
│
├── lru_cache.py
├── test_lru.py
├── benchmark.py
├── demo.py
├── README.md
├── report.md
└── requirements.txt
```

---

## Python Version

- Python 3.9 or above

No additional libraries need to be installed because the project only uses Python's standard library.

---

## Running the Project

To see how the cache works:

```bash
python demo.py
```

To run all unit tests:

```bash
python test_lru.py
```

To measure performance:

```bash
python benchmark.py
```

---

## Implementation Details

The cache is built using two data structures.

- A dictionary stores the cache entries and allows constant-time lookup.
- A doubly linked list maintains the order of recently used items.

Whenever an item is accessed, it is moved to the front of the list. If the cache becomes full, the item at the end of the list is removed because it is the least recently used.

To make the cache thread-safe, every `get()` and `put()` operation is protected using `threading.Lock`.

---

## Features

- Thread-safe cache implementation
- Constant-time `get()` and `put()` operations
- Automatic removal of the least recently used item
- Multi-threaded unit testing
- Performance benchmarking
- Simple demo program

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| get() | O(1) |
| put() | O(1) |
| Insert Node | O(1) |
| Remove Node | O(1) |

Space Complexity: **O(n)**, where **n** is the cache capacity.

---

## Testing

I tested the implementation using Python's `unittest` module.

The test cases cover:

- Basic insertion and retrieval
- Cache misses
- Updating existing keys
- LRU eviction
- Capacity validation
- Concurrent reads
- Concurrent writes
- Mixed read/write operations

All tests pass successfully.

---

## Benchmark

The benchmark compares the cache under different workloads:

- Read-heavy operations
- Write-heavy operations
- Mixed operations
- Multi-threaded execution

The execution time is measured using `time.perf_counter()`.

---

## Conclusion

This project helped me understand how an LRU Cache works internally and how synchronization is required when multiple threads access shared data. It also gave me practical experience with Python data structures, linked lists, thread synchronization, unit testing, and basic performance evaluation.
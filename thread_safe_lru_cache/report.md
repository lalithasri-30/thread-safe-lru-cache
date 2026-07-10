# Technical Report

# Thread-Safe LRU Cache in Python

## Introduction

As part of this project, I implemented a Thread-Safe Least Recently Used (LRU) Cache using Python. The main objective was to build a cache that supports fast `get()` and `put()` operations while allowing multiple threads to access it safely without causing data inconsistency.

While working on this project, I learned how different data structures can be combined to improve performance and how synchronization is important when multiple threads access shared data.

---

## Project Objective

The main objectives of this project are:

- Implement a thread-safe LRU Cache.
- Support O(1) time complexity for both `get()` and `put()` operations.
- Verify correctness using unit tests.
- Test the cache under multi-threaded conditions.
- Measure performance under different workloads.
- Explain the design decisions used in the implementation.

---

## Design Approach

Before writing the code, I studied how an LRU Cache works. I found that using only a dictionary would not be enough because it cannot maintain the order of recently used items.

To solve this problem, I combined two data structures:

- Dictionary
- Doubly Linked List

The dictionary stores references to cache entries, which makes searching for a key very fast.

The doubly linked list keeps track of which item was used recently. Whenever an item is accessed, it is moved to the front of the list. If the cache becomes full, the item at the end of the list is removed because it is the least recently used.

This combination makes both cache operations efficient.

---

## Thread Safety

Since the assignment requires a thread-safe cache, I used Python's `threading.Lock`.

Both `get()` and `put()` operations are protected using the same lock.

```python
with self.lock:
```

This ensures that only one thread modifies the cache at a time.

Using a lock prevents problems such as:

- Race conditions
- Incorrect cache updates
- Corrupted linked list structure

Although locking introduces a small delay when many threads are running together, it guarantees that the cache always remains in a valid state.

---

## Comparison of Locking Strategies

In this project I used `threading.Lock`, which works as a mutex.

A mutex allows only one thread to enter the critical section at a time. This makes the implementation simple and reliable.

Another possible approach is using a Reader-Writer Lock.

A Reader-Writer Lock allows multiple threads to read the cache simultaneously while write operations remain exclusive.

This approach may improve performance when the application performs many more read operations than write operations.

However, Python's standard library does not provide a built-in Reader-Writer Lock. For this reason, I selected `threading.Lock` because it is simple, easy to understand, and sufficient for this implementation.

---

## Cache Operations

### get(key)

When `get()` is called, the cache first checks whether the key exists.

If the key is available, the corresponding node is moved to the front of the linked list because it becomes the most recently used item.

If the key is not found, the method returns `-1`.

Time Complexity: **O(1)**

---

### put(key, value)

When `put()` is called, the cache first checks whether the key already exists.

If the key exists, its value is updated and the node is moved to the front.

If it is a new key, a new node is inserted.

If the cache exceeds its capacity, the least recently used item is removed automatically.

Time Complexity: **O(1)**

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

To verify that the implementation works correctly, I created multiple unit tests using Python's `unittest` module.

The tests cover:

- Basic insertion
- Data retrieval
- Cache miss
- Updating an existing key
- LRU eviction
- Capacity validation
- Large number of insertions
- Concurrent reads
- Concurrent writes
- Mixed thread operations

After running all the tests, every test case passed successfully.

---

## Performance Benchmark

I measured the cache performance using four different workloads.

| Workload | Execution Time (seconds) |
|-----------|-------------------------|
| Read Heavy | 0.006206 |
| Write Heavy | 0.006292 |
| Mixed | 0.006156 |
| Multi-threaded | 0.011007 |

*The execution time may vary depending on the computer used to run the program.*

---

## Performance Analysis

I observed that the read-heavy, write-heavy and mixed workloads completed in nearly the same amount of time.

This is expected because both `get()` and `put()` operations have constant-time complexity.

The multi-threaded benchmark took slightly longer. This happened because all threads share the same lock, so they sometimes have to wait before accessing the cache.

Even though locking adds a small amount of overhead, it ensures that the cache remains correct and thread-safe.

---

## Architectural Decisions

During development, I decided to use a dictionary together with a doubly linked list because each data structure solves a different problem.

The dictionary provides fast key lookup.

The doubly linked list efficiently maintains the order of recently used items.

Using both data structures together allows the cache to perform efficiently while keeping the implementation easy to understand.

---

## Memory Overhead

Compared to using only a dictionary, this implementation uses slightly more memory because every cache entry stores two additional pointers (`prev` and `next`) for the doubly linked list.

Although this increases memory usage, it allows nodes to be inserted, removed and moved in constant time.

I felt that this trade-off was acceptable because it improves the overall performance of the cache.

---

## Concurrency Trade-offs

Using a mutex provides reliable synchronization, but only one thread can update the cache at a time.

In applications with a very large number of threads, this may reduce performance slightly because some threads have to wait for the lock.

A Reader-Writer Lock could improve performance for read-heavy applications, but it would also make the implementation more complex.

For this project, using `threading.Lock` provided a good balance between simplicity, correctness and performance.

---

## Conclusion

This project helped me understand how an LRU Cache works internally and how thread synchronization is used in real applications.

By combining a dictionary, a doubly linked list and Python's `threading.Lock`, I was able to build a cache that supports O(1) operations while remaining safe for concurrent access.

The unit tests and benchmark results show that the implementation works correctly under different workloads.

Overall, this project gave me practical experience with data structures, multithreading, testing and performance evaluation in Python.

---

## Future Improvements

If I continue working on this project, I would like to:

- Implement a Reader-Writer Lock.
- Add cache hit and miss statistics.
- Support cache expiration (TTL).
- Benchmark with larger datasets.
- Explore asynchronous implementations using Python's async features.
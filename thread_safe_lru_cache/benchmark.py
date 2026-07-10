import random
import threading
import time
from lru_cache import LRUCache


NUM_OPERATIONS = 10000
CACHE_SIZE = 1000


def benchmark_read_heavy():
    cache = LRUCache(CACHE_SIZE)

    # Fill the cache first
    for i in range(CACHE_SIZE):
        cache.put(i, i)

    start = time.perf_counter()

    for _ in range(NUM_OPERATIONS):
        if random.random() < 0.9:
            cache.get(random.randint(0, CACHE_SIZE - 1))
        else:
            key = random.randint(0, CACHE_SIZE - 1)
            cache.put(key, key)

    end = time.perf_counter()

    return end - start


def benchmark_write_heavy():
    cache = LRUCache(CACHE_SIZE)

    start = time.perf_counter()

    for i in range(NUM_OPERATIONS):
        if random.random() < 0.9:
            cache.put(i, i)
        else:
            cache.get(random.randint(0, i if i > 0 else 0))

    end = time.perf_counter()

    return end - start


def benchmark_mixed():
    cache = LRUCache(CACHE_SIZE)

    start = time.perf_counter()

    for i in range(NUM_OPERATIONS):
        if random.random() < 0.5:
            cache.put(i, i)
        else:
            cache.get(random.randint(0, i if i > 0 else 0))

    end = time.perf_counter()

    return end - start


def worker(cache, start_index):
    for i in range(start_index, start_index + 2000):
        cache.put(i, i)
        cache.get(i)


def benchmark_multithread():
    cache = LRUCache(CACHE_SIZE)

    threads = []

    start = time.perf_counter()

    for i in range(5):
        t = threading.Thread(target=worker, args=(cache, i * 2000))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()

    return end - start


def print_results():
    read_time = benchmark_read_heavy()
    write_time = benchmark_write_heavy()
    mixed_time = benchmark_mixed()
    multi_time = benchmark_multithread()

    print("\n========== Performance Benchmark ==========\n")
    print(f"{'Workload':<20}{'Time (seconds)'}")
    print("-" * 35)
    print(f"{'Read Heavy':<20}{read_time:.6f}")
    print(f"{'Write Heavy':<20}{write_time:.6f}")
    print(f"{'Mixed':<20}{mixed_time:.6f}")
    print(f"{'Multi-threaded':<20}{multi_time:.6f}")


if __name__ == "__main__":
    print_results()
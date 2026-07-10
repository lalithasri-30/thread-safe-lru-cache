import unittest
import threading
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_put_and_get(self):
        cache = LRUCache(2)
        cache.put(1, "Apple")
        self.assertEqual(cache.get(1), "Apple")

    def test_cache_miss(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(100), -1)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, "Apple")
        cache.put(1, "Orange")
        self.assertEqual(cache.get(1), "Orange")

    def test_lru_eviction(self):
        cache = LRUCache(2)

        cache.put(1, "A")
        cache.put(2, "B")
        cache.put(3, "C")

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), "B")
        self.assertEqual(cache.get(3), "C")

    def test_recently_used(self):
        cache = LRUCache(2)

        cache.put(1, "A")
        cache.put(2, "B")

        cache.get(1)

        cache.put(3, "C")

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), "A")

    def test_capacity_one(self):
        cache = LRUCache(1)

        cache.put(1, "A")
        cache.put(2, "B")

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), "B")

    def test_contains(self):
        cache = LRUCache(2)
        cache.put(1, "Apple")

        self.assertTrue(1 in cache)
        self.assertFalse(2 in cache)

    def test_large_insertions(self):
        cache = LRUCache(100)

        for i in range(1000):
            cache.put(i, i)

        self.assertEqual(len(cache), 100)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            LRUCache(0)

    def test_concurrent_writes(self):

        cache = LRUCache(50)

        def writer(start):
            for i in range(start, start + 100):
                cache.put(i, i)

        threads = []

        for i in range(5):
            t = threading.Thread(target=writer, args=(i * 100,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        self.assertLessEqual(len(cache), 50)

    def test_concurrent_reads(self):

        cache = LRUCache(100)

        for i in range(100):
            cache.put(i, i)

        def reader():
            for i in range(100):
                cache.get(i)

        threads = []

        for _ in range(10):
            t = threading.Thread(target=reader)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        self.assertEqual(len(cache), 100)

    def test_mixed_operations(self):

        cache = LRUCache(20)

        def worker(start):
            for i in range(start, start + 50):
                cache.put(i, i)
                cache.get(i)

        threads = []

        for i in range(5):
            t = threading.Thread(target=worker, args=(i * 50,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        self.assertLessEqual(len(cache), 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)
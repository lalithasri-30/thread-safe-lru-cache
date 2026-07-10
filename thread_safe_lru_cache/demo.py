from lru_cache import LRUCache


def main():
    print("=" * 50)
    print("Thread-Safe LRU Cache Demonstration")
    print("=" * 50)

    cache = LRUCache(3)

    print("\nAdding items...")
    cache.put(1, "Apple")
    cache.put(2, "Banana")
    cache.put(3, "Mango")

    cache.display_cache()

    print("\nAccessing key 1")
    print("Value:", cache.get(1))

    cache.display_cache()

    print("\nAdding key 4 (Orange)")
    cache.put(4, "Orange")

    print("\nLeast Recently Used item has been evicted.")

    cache.display_cache()

    print("\nSearching for key 2")
    print("Result:", cache.get(2))

    print("\nSearching for key 4")
    print("Result:", cache.get(4))

    print("\nDemo Completed Successfully!")


if __name__ == "__main__":
    main()
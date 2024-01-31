#!/usr/bin/env python3
"""
FIFO caching script
"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching implementation"""

    def __init__(self):
        """Initialisation"""

        super().__init__()

    def put(self, key, item):
        """Stores item to the cache"""

        if item is not None and key is not None:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data.keys()
            ):
                firstIn = next(iter(self.cache_data.keys()))
                del self.cache_data[firstIn]
                print(f"DISCARD: {firstIn}")

                self.cache_data[key] = item

    def get(self, key):
        """ "Returns cached item given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

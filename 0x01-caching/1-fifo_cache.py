#!/usr/bin/env python3
"""
caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    cache
    """

    def __init__(self):
        """
        initialisation
        """
        super().__init__()

    def put(self, key, item):
        """
        put method
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                firstkey = next(iter(self.cache_data.keys()))
                del self.cache_data[firstkey]
                print("DISCARD: {}". format(firstkey))

            self.cache_data[key] = item

    def get(self, key):
        """
        get methods
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

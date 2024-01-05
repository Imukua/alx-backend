#!/usr/bin/env python3
"""
Basecache class
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    base class
    """

    def __init__(self):
        """
        initialisation
        """
        super().__init__()

    def put(self, key, item):
        """
        put methods
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        get methods
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

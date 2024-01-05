#!/usr/bin/env python3
"""
caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    caching
    """

    def __init__(self):
        """
        initialisation
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                d = self.usedKeys.pop(-2)
                del self.cache_data[d]
                print('DISCARD: {:s}'.format(d))

    def get(self, key):
        """
        get method
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None

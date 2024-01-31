#!/usr/bin/env python3
"""
implements put and get caching methods
."""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Base cache class
    """

    def __init__(self):
        """Initialisation"""

        super().__init__()

    def put(self, key, item):
        """Puts items into the cache."""

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns cached item"""
        return self.cache_data.get(key)

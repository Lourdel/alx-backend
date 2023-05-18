#!/usr/bin/env  python3
"""Module defines class BasicCache"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """implementation of basic cache"""
    def __init__(self):
        """Iniatalise"""
        super().__init__()

    def put(self, key, item):
        """Method adds an item to cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Method retrieves an item from cache by key"""
        return self.cache_data.get(key)

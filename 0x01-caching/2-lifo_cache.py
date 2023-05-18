#!/usr/bin/env python3
"""Module defines class LIFOCache that inherits from BaseCaching"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Method implements LIFO cache policy"""
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Method adds an item to cache"""
        if key and item:
            self.cache_data[key] = item
            if key in self.stack:
                self.stack.remove(key)
            self.stack.append(key)

        if len(self.stack) > self.MAX_ITEMS:
            popped_items = self.stack.pop(-2)
            del self.cache_data[popped_items]
            print(f"DISCARD: {popped_items}")

    def get(self, key):
        """Method retrieves an item from cache by key"""
        return self.cache_data.get(key)

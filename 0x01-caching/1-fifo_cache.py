#!/usr/bin/env python3
"""Module defines class FIFOCache that inherits from BaseCaching"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Method implements FIFO cache policy"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Method adds an item to cache"""
        if key and item:
            self.cache_data[key] = item
            if key not in self.queue:
                self.queue.append(key)

        if len(self.queue) > self.MAX_ITEMS:
            popped_items = self.queue.pop(0)
            del self.cache_data[popped_items]
            print(f"DISCARD: {popped_items}")

    def get(self, key):
        """Method retrieves an item from cache by key"""
        return self.cache_data.get(key)

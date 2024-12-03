#!/usr/bin/python3
""" LRU Cache module """
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    inherits from BasicCaching and performs
    LRU caching mechanism
    """

    def __init__(self):
        """
        initialize LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        adds an item to the LRUcache
        """

        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_used = self.order.pop(0)
                del self.cache_data[least_used]
                print(f"DISCARD: {least_used}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        returns the selected item using key given
        if key exists mark it as recently used
        """

        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
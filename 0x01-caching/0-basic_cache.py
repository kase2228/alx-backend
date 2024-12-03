#!/usr/bin/env python3
"""simple cache
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """simple cache iherits from BaseCaching
    """

    def put(self, key, item):
        """adds an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        retrive an item from the cache in a given key
        and if key is none or doesn't exist return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
    
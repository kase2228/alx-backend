#!/usr/bin/python3
""" MRU Cache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    inherits from BaseCaching and performs
    MRU caching mechanism
    """

    def __init__(self):
        """
        initialize the MRUCache
        """
        super().__init__()
        self.most_recent = None

    def put(self, key, item):
        """
        add an item to the MRUCache
        """

        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print(f"DISCARD: {self.most_recent}")
                    del self.cache_data[self.most_recent]
                self.cache_data[key] = item

            self.most_recent = key

    def get(self, key):
        """
        get an item from the cache using key
        if key exists marked as most recently used
        """

        if key in self.cache_data:
            self.most_recent = key
            return self.cache_data[key]

        return None

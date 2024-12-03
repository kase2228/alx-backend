#!/usr/bin/python3
""" LIFO Cache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and 
    perform LIFO caching Mechanism
    """

    def __init__(self):
        """
        initialize LIFOCache
        """

        super().__init__()
        self.last_key = None

    def put(self, key ,item):
        """
        add an item in LIFOCahing mechanism
        """

        if key is not None and item is not None:
            if len(self.cache_data
                   ) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        return an item using the given key
        """

        return self.cache_data.get(key, None)

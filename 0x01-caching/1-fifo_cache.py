#!/usr/bin/python3
""" FIFO Cache module """
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    inherits from Basecaching and perform
    FIFO caching mechanism
    """

    def __init__(self):
        """initialize the FIFOCache"""

        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        add an item to the cache using a fifo method
        i.e if cache exceed limit remove oldest
        """

        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest = self.order.pop(0)
                del self.cache_data[oldest]
                print(f"DISCARD: {oldest}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        get an item by key
        if key none or doesn't exist return None
        """

        return self.cache_data.get(key, None)

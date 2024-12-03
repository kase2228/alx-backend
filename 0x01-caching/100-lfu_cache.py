#!/usr/bin/python3
""" LFU Cache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and implements an LFU caching mechanism.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        Calls the parent class constructor and sets up tracking dictionaries.
        """
        super().__init__()
        self.freq_tracker = {}  # Tracks the frequency of each key
        self.usage_tracker = {}  # Tracks the order of usage for LRU handling

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, do nothing.
        Implements LFU by removing the least frequently used key, using LRU as a tie-breaker.
        """
        if key is None or item is None:
            return

        # If the key already exists, just update the value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_tracker[key] += 1
            self.usage_tracker[key] = len(self.usage_tracker)  # Update usage order
        else:
            # If the cache is full, remove the LFU (and LRU in case of ties)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU key(s)
                min_freq = min(self.freq_tracker.values())
                lfu_keys = [k for k, v in self.freq_tracker.items() if v == min_freq]

                # If there's a tie, use LRU to decide
                if len(lfu_keys) > 1:
                    lfu_key = min(lfu_keys, key=lambda k: self.usage_tracker[k])
                else:
                    lfu_key = lfu_keys[0]

                # Remove the LFU/LRU key
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.freq_tracker[lfu_key]
                del self.usage_tracker[lfu_key]

            # Add the new key
            self.cache_data[key] = item
            self.freq_tracker[key] = 1  # New key starts with a frequency of 1
            self.usage_tracker[key] = len(self.usage_tracker)  # Add to the usage tracker

    def get(self, key):
        """
        Get an item by key from the cache.
        If the key exists, increment its frequency and update its usage order.
        Returns None if the key is None or doesn't exist.
        """
        if key in self.cache_data:
            self.freq_tracker[key] += 1  # Increment the frequency
            self.usage_tracker[key] = len(self.usage_tracker)  # Update usage order
            return self.cache_data[key]
        return None

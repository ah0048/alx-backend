#!/usr/bin/python3
''' LRU Caching'''
from base_caching import BaseCaching
from functools import lru_cache


class LRUCache(BaseCaching):
    ''' LRUCache class that inherits from BaseCaching
    and is a caching system'''

    def __init__(self):
        super().__init__()
        self.least_recently_used = []

    def put(self, key, item):
        ''' Add an item in the cache'''
        if key and item:
            if key in self.cache_data:
                self.least_recently_used.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.least_recently_used.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.least_recently_used.append(key)

    def get(self, key):
        ''' Get an item by key'''
        if key in self.cache_data:
            self.least_recently_used.remove(key)
            self.least_recently_used.append(key)
            return self.cache_data.get(key)
        return None

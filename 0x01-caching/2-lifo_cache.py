#!/usr/bin/python3
''' LIFO caching'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCache class that inherits from BaseCaching
    and is a caching system'''

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        ''' Add an item in the cache'''
        if key and item:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        ''' Get an item by key'''
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None

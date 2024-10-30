#!/usr/bin/python3
''' FIFO caching'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFOCache class that inherits from BaseCaching
    and is a caching system'''
    def put(self, key, item):
        ''' Add an item in the cache'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key'''
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None

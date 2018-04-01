class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.key = []
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.key.remove(key)
            self.key.insert(0, key)
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.key.remove(key)
            self.key.insert(0, key)
            self.cache[key] = value
        elif len(self.key) == self.capacity:
            old_key = self.key.pop()
            self.cache.pop(old_key)
            self.key.insert(0, key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.key.insert(0, key)
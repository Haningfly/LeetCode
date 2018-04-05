class HashTable(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [[] for x in range(capacity)]

    def get(self, key):
        hash_value = self.hash(key)
        if not self.items[hash_value]:
            return None

        item_list = self.items[hash_value]
        for item in item_list:
            if item[0] == key:
                return item[1]

        return None

    def set(self, key, value):
        hash_value = self.hash(key)
        item_list = self.items[hash_value]
        for item in item_list:
            if item[0] == key:
                item_list.remove(item)

        item_list.insert(0, (key, value))

    def hash(self, key):
        return key % self.capacity

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)
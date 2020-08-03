class DesignHashSet(object):
    def __init__(self):
        self.hashset = [None] * 10000

    def hash(self, key):
        return key % 10000

    def add(self, key):
        if self.contains(key):
            return
        idx = self.hash(key)
        if self.hashset[idx] is None:
            self.hashset[idx] = [key]
        else:
            self.hashset[idx].append(key)

    def remove(self, key):
        if not self.contains(key):
            return
        idx = self.hash(key)
        if self.hashset[idx] is not None:
            arr = self.hashset[idx]
            del arr[arr.index(key)]

    def contains(self, key):
        idx = self.hash(key)
        if self.hashset[idx] is None:
            return None
        else:
            arr = self.hashset[idx]
            print(self.hashset)
            print(arr)
            return any(val == key for val in arr)

if __name__ == "__main__":
    hashSet = DesignHashSet()
    hashSet.add(1)
    hashSet.add(2)

    hashSet.contains(2)

    #print(hashSet.hashset)
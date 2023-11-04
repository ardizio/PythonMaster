class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.data = [None] * size

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.data[index] is None:
            self.data[index] = []
        self.data[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            for k, v in self.data[index]:
                if k == key:
                    return v
        return None

    def remove(self, key):
        index = self._hash(key)
        if self.data[index] is not None:
            for i, (k, v) in enumerate(self.data[index]):
                if k == key:
                    del self.data[index][i]
                    return

# Example usage of the HashMap class
my_map = HashMap()

my_map.put("name", "Alice")
my_map.put("age", 25)

print(my_map.get("name"))  # Output: Alice
print(my_map.get("age"))   # Output: 25

my_map.remove("name")
print(my_map.get("name"))  # Output: None
print(my_map.get("age"))  # Output: None


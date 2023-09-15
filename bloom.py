import math
import mmh3

class BloomFilter:
    def __init__(self, capacity, error_rate):
        self.capacity = capacity
        self.error_rate = error_rate
        self.bit_array_size = self.calculate_bit_array_size()
        self.hash_functions = self.calculate_hash_functions()
        self.bit_array = [False] * self.bit_array_size

    def calculate_bit_array_size(self):
        # Formula to calculate the optimal bit array size
        return int(-(self.capacity * math.log(self.error_rate)) / (math.log(2) ** 2))

    def calculate_hash_functions(self):
        # Number of hash functions required
        k = int((self.bit_array_size / self.capacity) * math.log(2))
        return [lambda x, i=i: mmh3.hash(x, i) % self.bit_array_size for i in range(k)]

    def add(self, item):
        for hash_function in self.hash_functions:
            index = hash_function(item)
            self.bit_array[index] = True

    def contains(self, item):
        for hash_function in self.hash_functions:
            index = hash_function(item)
            if not self.bit_array[index]:
                return False
        return True

if __name__ == "__main__":
    capacity = 1000  # Maximum number of elements in the set
    error_rate = 0.01  # Acceptable false positive rate
    errors = [1.,.5,.25,.1,.01]
    for error_rate in errors:
        print("/********************************************/")
        print("Calculating for error rate:" + str(error_rate))
        print("/********************************************/")
        bloom_filter = BloomFilter(capacity, error_rate)

        # Add items to the Bloom filter
        items_to_add = ["apple", "banana", "cherry", "date", "elderberry"]
        for item in items_to_add:
            bloom_filter.add(item)

        # Check if an item is in the Bloom filter
        items_to_check = ["apple", "grape", "kiwi", "lemon", "avocado", "drape", "applex"]
        for item in items_to_check:
            print(item)
            if bloom_filter.contains(item):
                print(f"'{item}' is in the Bloom filter (may be a false positive).")
            else:
                print(f"'{item}' is not in the Bloom filter.")

        print("/********************************************/")

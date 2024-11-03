from tabulate import tabulate


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index][i] = (key, value)
                return
        self.table[hash_index].append((key, value))

    def get(self, key):
        hash_index = self._hash(key)
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_index = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                del self.table[hash_index][i]
                return True
        return False

    def __str__(self):
        table_data = []
        for i, bucket in enumerate(self.table):
            for k, v in bucket:
                table_data.append([i, k, v])
        return tabulate(table_data, headers=["Index", "Key", "Value"], tablefmt="grid")


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.insert("apple", 10)
    hash_table.insert("banana", 20)
    hash_table.insert("grape", 30)
    print("Початкова таблиця:")
    print(hash_table)

    hash_table.delete("banana")
    print("\nПісля видалення 'banana':")
    print(hash_table)

    result = hash_table.delete("orange")
    print("\nВидалення неіснуючого елемента 'orange':", result)
    print("\nПоточна таблиця:")
    print(hash_table)

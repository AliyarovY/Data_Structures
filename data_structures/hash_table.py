class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size


    def custom_hash(self, key):
        return sum(ord(x) for x in str(key)) % self.table_size


    def add_key_value(self, key, value):
        index = self.custom_hash(key)
        position = self.hash_table[index]

        if isinstance(position, list):
            for i, j in enumerate(position):
                k, v = j
                if k == key:
                    self.hash_table[index][i] = (key, value)
                    break

            self.hash_table[index].append((key, value))

        elif position:
            if position[0] == key:
                self.hash_table[index] = (key, value)
                return
            self.hash_table[index] = [position, (key, value)]

        else:
            self.hash_table[index] = (key, value)


    def get_value(self, key):
        ind = self.custom_hash(key)
        position = self.hash_table[ind]

        if isinstance(position, list):
            for k, v in position:
                if k == key:
                    return v

        if not position:
            return False

        return position[1]



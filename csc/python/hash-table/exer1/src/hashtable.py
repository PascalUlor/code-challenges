# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        unsigned long
        hash(unsigned char *str)
        {
        unsigned long hash = 5381;
        int c;

        while (c = *str++)
            hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

        return hash;
        }


        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # pass
        # new_item = LinkedPair(key, value)
        hashed_key = self._hash_mod(key)
        if self.storage[hashed_key] is None:
            # print("Adding new bucket with key " + key)
            self.storage[hashed_key] = LinkedPair(key, value)
        else:
            slot = self.storage[hashed_key]
            head = slot
            while slot is not None:
                if slot.key == key:
                    # print("Overwriting key " + key)
                    slot.value = value
                    return
                slot = slot.next
            # print("Adding new key to bucket " + key)
            new_slot = LinkedPair(key, value)
            self.storage[hashed_key] = new_slot
            new_slot.next = head

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # pass
        hashed_key = self._hash_mod(key)
        if self.storage[hashed_key] is None:
            print('Key does not exist')
        else:
            self.storage[hashed_key] = None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # pass
        hashed_key = self._hash_mod(key)
        if self.storage[hashed_key] is None:
            return None
        else:
            slot = self.storage[hashed_key]
            while slot is not None:
                if slot.key == key:
                    return slot.value
                slot = slot.next
                # return slot.value
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # pass
        self.capacity *= 2
        prev_storage = self.storage
        self.storage = [None] * self.capacity
        for node in prev_storage:
            if node is not None:
                current_node = node
                while current_node:
                    self.insert(current_node.key, current_node.value)
                    current_node = current_node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

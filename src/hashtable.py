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


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

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

        hashed_key = self._hash_mod(key)
        if self.storage[hashed_key] is None:
            self.storage[hashed_key] = LinkedPair(key , value)
        else:
            entry = self.storage[hashed_key]
            while entry and entry.key != key:
                prev, entry = entry, entry.next
            if entry:
                entry.value = value
            else:
               prev.next =  LinkedPair(key , value)
  

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        entry = self.storage[hashed_key]
        prev = None
        while entry and entry.key != key:
            prev , entry = entry , entry.next
        if entry is None:
            print("Key does not exist")
        else:
            if prev is None:
                self.storage[hashed_key] = entry.next
            else:
                prev.next = entry.next



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.


        Returns None if the key is not found.

        Fill this in.
        '''
        entry = self.storage[self._hash_mod(key)]
        if not entry:
            return None
        while entry and entry.key !=key :
                entry = entry.next
        return entry.value
  

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = [None] * self.capacity * 2
        for i in range(self.capacity):
            new_storage[i] = self.storage[i]
        self.storage = new_storage




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

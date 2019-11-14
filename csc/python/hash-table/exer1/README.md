
# Hash Tables in Python

Hash tables are arguably the single most important data structures in existence. Used to implement everything from objects in JavaScript and dictionaries in Python to Memcached over a distributed computer network, hash tables are beloved by programmers for providing key/value storage with constant big-O time complexity for insertion, deletion, and access.

## What is a hash table?

Underneath the hood, a hash table is simply an array with its elements indexed by a hashed key. Like arrays, hash tables are initialized to a fixed size and inserting, deleting, and reading elements within those boundaries can be accomplished in constant time, or O(1).

![Hash Table](img/HashTableImage.png)

In this diagram, you can see the key (a string) is run through a hash function which produces an integer 0-15 which is used as the index in a 16-element array.

## What is a hash function?

Hash functions map data of an arbitrary size to data of a fixed size. For example, a size-16 hash function might hash string-typed keys like so:

`"foo"` -> `10`

`"bar"` -> `12`

`"baz"` -> `5`

`"Hello world!"` -> `6`

`"Very long keys can hash be hashed as well"` -> `10`

In this way, keys of any length can be mapped to an integer value which can be used as an array index for a hash table. Note that since there are an infinite amount of possible keys that must map to only 16 possible indices, values with different keys will inevitably collide.

There are many different types of hash functions with different uses (you may have come across cryptographic hashes for storing passwords in a database) but they generally have a few common characteristics:

1. Deterministic: For a given input, the output will always be the same.
2. Defined output range: For a hash table of size 16, all keys must hash to a value 0-15. For smaller values, this is usually accomplished using the modulo `%` operation.
3. Predictable Speed: Hash functions for hash tables should be lightning fast while cryptographic hashes (like bcrypt) should be very slow.
4. Non-invertible: You should not be able to reconstruct the input value from the output. This trait is important in cryptographic hashes but not necessary for general hash tables.

## How are hash table collisions handled?

There are many ways to handle [hash table collisions](https://en.wikipedia.org/wiki/Hash_table#Collision_resolution) but we'll focus on the linked list chaining method.

Let's say we have a hash table of size 4 and we are adding 5 elements like so:

`ht["a"] = "aardvark"`

`ht["b"] = "bear"`

`ht["c"] = "cat"`

`ht["d"] = "dog"`

`ht["e"] = "elephant"`

Now, let's say our hash function maps the keys like so:

`"a"` -> `0`

`"b"` -> `1`

`"c"` -> `2`

`"d"` -> `3`

`"e"` -> `2`

Our array would look something like this:

`0` = `<"a", "aardvark">  ->  NULL`

`1` = `<"b", "bear">  ->  NULL`

`2` = `<"c", "cat">  ->  <"e", "elephant">  ->  NULL`

`3` = `<"d", "dog">  ->  NULL`

Now if we want to find the value stored for "e", we would first find it's hashed index (2), then travel through the linked list until we find the key/value pair with a matching key and return the value.

Note that while searching with a hashed index has time complexity of O(1), searching through a linked list has O(n). This is why sparsely populated hash tables have search/insert/delete of O(1), performance will degrade as they fill up and they can have a worst-case performance of O(n) if every single key happens to hash to the same value.

## How do we prevent performance from degrading when the hash table fills up?

Due to this performance degradation, most languages, such as Python, will automatically resize the hash table when it reaches a certain capacity. This is done by creating a new hash table (usually doubling in size) and copying each element one-by-one into the new hash table.


# Assignment

Your assignment is to implement a hash table in Python. You should be able to insert, read, and delete elements and handle hash collisions with linked list chaining. You should be able to insert an arbitrary amount of elements into your hash table, regardless of storage size, and read them back without any data loss. You should also implement a resizing function that doubles the size of your hash table and copies all elements into the new data structure.

Run your code by typing `python hashtable.py`.

Run tests by typing `python test_hashtable.py`.

## STRETCH GOALS
1. Research and implement the DJB2 hashing algorithm.

2. Update your HashTable to automatically double in size when it grows past a load factor of 0.7 and half in size when it shrinks past a load factor of 0.2. This should only occur if the HashTable has been resized past the initial size. Refactor tests to pass with your resizing HashTable.

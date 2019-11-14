### General

* [Why do I need to know how a Hash Table works?](#q100)
* [What's the difference between a HashTable and a Dictionary?](#q101)
* [What's the difference between a HashTable and a Set/HashSet?](#q102)
* [What's the difference between a HashTable and a HashMap?](#q103)
* [What's the difference between a HashTable and an Object (JavaScript)?](#q104)
* [What's the difference between a HashTable and a Cache?](#q105)


<a name="q100"></a>
### Why do I need to know how a Hash Table works?
Hash tables are performant, elegant and simple. If you're looking to speed up some code, it's very likely that some form of Hash Table or caching is the answer.

<a name="q101"></a>
### What's the difference between a HashTable and a Dictionary?
A dictionary is a dynamic HashTable implementation that automatically handles sizing and resizing of the underlying array structure. Dictionaries show up in languages like Python, Java, Swift, Kotlin and more.

<a name="q102"></a>
### What's the difference between a HashTable and a Set/HashSet?
Sets, sometimes known as HashSets, are HashTable implementations that store data as an unordered collection of keys without values. Sets have the same O(1) insert, delete and search as Hash Tables with no implicit ordering and no duplicates. If you think about how Hash Tables store keys, you'll understand why Sets must be unordered and have no duplicates.

<a name="q103"></a>
### What's the difference between a HashTable and a HashMap?
HashMaps are dynamic HashTable implementation with some very minor language-specific differences. You can view this (link)[https://stackoverflow.com/questions/40471/differences-between-hashmap-and-hashtable] for more details.

<a name="q104"></a>
### What's the difference between a HashTable and an Object (JavaScript)?
Objects are a JavaScript implementation of a HashTable. Virtually everything in JavaScript is stored as an Object. Closely related to Objects is JSON, or JavaScript Object Notation. This is a text representation of nested Objects and Arrays stored as text. Note that JSON must be Parsed to become an Object, then Stringified to return to a string for transport and storage.

<a name="q105"></a>
### What's the difference between a HashTable and a Cache?
Cache is just a name for fast data storage. These can take many forms but the most common is key/value storage using a Hash Table.

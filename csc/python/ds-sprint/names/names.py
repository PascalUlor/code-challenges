from binary_search_tree import BinarySearchTree
import time
import sys

start_time = time.time()

f = open('names_1.txt', 'r')  # O(c)
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')  # O(c)
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1: #O(n)
#     for name_2 in names_2: #O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1) #O(c)
# check = BinarySearchTree(names_1[0])
check = dict()
for name_1 in names_1:
    check[name_1] = True
for name_2 in names_2:
    if name_2 in check:
        duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

"""
Runtime of first solution has a runtime of O(n^2)
New solution has a runtime of O(n)
"""

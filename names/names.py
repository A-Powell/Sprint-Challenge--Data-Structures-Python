import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements -
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# binary_tree = BinarySearchTree(names_1[0])

# for i in range(1, len(names_1)):
#     binary_tree.insert(names_1[i])

# for i in range(0, len(names_2)):
#     if binary_tree.contains(names_2[i]):
#         duplicates.append(names_2[i])

binary_tree = BinarySearchTree('names')

for names in names_1:
    binary_tree.insert(names)

for name in names_2:
    if binary_tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# runtime: 13.547685384750366 seconds <--------- Initial - O(n^2)

# runtime: 0.18688392639160156 seconds  - O(logn)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

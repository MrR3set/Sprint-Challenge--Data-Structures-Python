import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

tree = BSTNode("Jean Peterson")


# Replace the nested for loops below with your improvements
for names in names_1:
    tree.insert(names)
for names in names_2:
    if tree.contains(names):
        duplicates.append(names)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

---------- Stretch Goal -----------
Python has built-in tools that allow for a very efficient approach to this problem
What's the best time you can accomplish?  Thare are no restrictions on techniques or data
structures, but you may not import any additional libraries that you did not write yourself.



# import time
# from binary_search_tree import BSTNode
# import threading

# start_time = time.time()

# names_1 = []
# names_2 = []

# def filereader(filename,storage):
#     f = open(str(filename), 'r')
#     storage.extend(f.read().split("\n"))  # List containing 10000 names
#     f.close()
    
# t1 = threading.Thread(target=filereader("names_1.txt",names_1))
# t2 = threading.Thread(target=filereader("names_2.txt",names_2))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# duplicates = []  # Return the list of duplicates in this data structure

# tree = BSTNode("John Kang")

# # Replace the nested for loops below with your improvements
# for names in names_1:
#     tree.insert(names)
# for names in names_2:
#     if tree.contains(names):
#         duplicates.append(names)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# # ---------- Stretch Goal -----------
# # Python has built-in tools that allow for a very efficient approach to this problem
# # What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# # structures, but you may not import any additional libraries that you did not write yourself.

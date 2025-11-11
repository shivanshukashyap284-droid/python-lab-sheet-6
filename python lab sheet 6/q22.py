my_list = [1, 2, 2, 3, 4, 4, 5]
duplicates = set([x for x in my_list if my_list.count(x) > 1])
print("Duplicate elements:", duplicates)

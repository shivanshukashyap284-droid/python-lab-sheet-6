from itertools import chain, combinations

def power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

my_set = {1, 2, 3}
print("Power set:", power_set(my_set))

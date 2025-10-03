# List manipulation
def remove_duplicates(lst):
    return list(set(lst))

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

# Tuple example
def swap_tuple_elements(t):
    a, b = t
    return (b, a)

# Dictionary operations
def count_frequency(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

def invert_dict(d):
    return {v: k for k, v in d.items()}

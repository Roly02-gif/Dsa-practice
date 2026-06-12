from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    num_occ = {}
    for num in arr:
        num_occ.setdefault(num, None)
        num_occ[num] = 1 if num_occ[num] is None else num_occ[num]+1

    set_occ = set(num_occ.values())
    return len(num_occ) == len(set_occ) 
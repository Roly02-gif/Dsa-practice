from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    n = len(grid)
    cols = []
    for i in range(n):
        col = []
        for j in range(n):
            col.append(grid[j][i])
        cols.append(col)
    
    pairs = 0
    for col in cols:
        b = grid.count(col)
        pairs += b
    return pairs
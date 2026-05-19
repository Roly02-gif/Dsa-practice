from typing import List


# Solution 1: Brute Force --- O(n^2)
def maxArea(height: List[int]) -> int:
    res = []
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            vol = (j - i) * min(height[i], height[j])
            res.append(vol)
    return max(res)


# Solution 2: Two Pointers --- O(n)
def maxArea(height: List[int]) -> int:
    res = 0
    i = 0
    j = len(height) - 1
    while i <= j:
        vol = (j - i) * min(height[i], height[j])
        res = vol if vol > res else res
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res

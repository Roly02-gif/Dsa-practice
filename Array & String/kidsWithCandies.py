from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    n = len(candies)
    result = [True] * n
    greatest_num = max(candies)
    for i in range(n):
        result[i] = candies[i] + extraCandies >= greatest_num
    return result

from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
        n = len(nums)
        sum_num = sum(nums[:k])
        res = sum_num/k
        for i in range(n-k):
            sum_num = sum_num - nums[i] + nums[i+k]
            res = max(sum_num/k, res)
        return res
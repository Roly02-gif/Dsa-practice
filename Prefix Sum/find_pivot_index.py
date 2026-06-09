from typing import List


def pivotIndex(nums: List[int]) -> int:
        tot = sum(nums)
        tot_l = 0
        for i in range(len(nums)):
            tot_r = tot - tot_l - nums[i]

            if tot_l == tot_r:
                return i
            
            tot_l += nums[i]
        return -1
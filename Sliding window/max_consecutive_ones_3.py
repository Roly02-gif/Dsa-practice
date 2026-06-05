from typing import List


def longestOnes(nums: List[int], k: int) -> int:
        res = 0
        i = 0
        j = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i +=1
            
            res = max(j-i+1, res)
        return res
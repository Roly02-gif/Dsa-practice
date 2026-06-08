from ast import List


def longestSubarray(nums: List[int]) -> int:
        count_zero = 0
        i = 0
        j = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                count_zero += 1
            
            if count_zero > 1 :
                if nums[i] == 0:
                    count_zero -= 1
                i += 1
            
            res = max(j-i, res)
        return res
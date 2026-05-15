from typing import List


# solution 1
def increasingTriplet(nums: List[int]) -> bool:
    f = nums[0]
    s = None
    for i in range(1, len(nums)):
        if nums[i] <= f:
            f = nums[i]
        elif s is None:
            s = nums[i]
        elif nums[i] <= s:
            s = nums[i]
        else:
            return True
    return False


# Solution 2
def increasingTriplet(nums: List[int]) -> bool:
    f = s = float("inf")
    for n in nums:
        if n <= f:
            f = n
        elif n <= s:
            s = n
        else:
            return True
    return False

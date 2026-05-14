from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    pre = 1
    for i in range(0, n):
        answer[i] = pre
        pre *= nums[i]
    suf = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suf
        suf *= nums[i]
    return answer


print(productExceptSelf([1, 2, 3, 4]))

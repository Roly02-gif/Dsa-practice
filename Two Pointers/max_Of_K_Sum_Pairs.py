from typing import Counter, List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums1 = [k - n for n in nums if k > n]
        i = 0
        j = len(nums1) - 1
        count = 0
        while i < len(nums) and j >= 0:
            if nums[i] == nums1[j]:
                count += 1
                i += 1
                j -= 1
            elif nums[i] > nums1[j]:
                j -= 1
            else:
                i += 1
        return count // 2


# print(Solution().maxOperations([1, 2, 3, 4], 5))
a = [1, 2, 3, 4]
print(Counter(a))

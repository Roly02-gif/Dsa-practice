from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    merged = []
    nums1 = nums1[:m]
    if n == 0:
        return nums1
    if m == 0:
        return nums2
    while nums1 != [] and nums2 != []:
        if nums1[0] <= nums2[0]:
            merged.append(nums1[0])
            nums1.pop(0)
        else:
            merged.append(nums2[0])
            nums2.pop(0)
    merged.extend(nums2) if nums1 == [] else merged.extend(nums1)
    return merged


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [9, 2, 5, 6].sort()
n = 3
# print(merge(nums1, m, nums2, n))
print(nums2)

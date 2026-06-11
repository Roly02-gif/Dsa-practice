from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    ans_one = set([elt for elt in nums1 if elt not in nums2])
    ans_two = set([elt for elt in nums2 if elt not in nums1])
    return [list(ans_one), list(ans_two)]
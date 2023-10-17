# Two-Pass Hash Tables
# Runtime: 40ms & Memory: 14.11MB
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    di = {}
    for i, val in enumerate(nums):
        result = target - val
        if result in di:
            return [di[result], i]
        else:
            di[val] = i
    return []

# 对分查找 迭代查找
from common import cost


# @cost
def dac_t(nums, target):
    # 2 1
    # 4 2
    # 8 3
    # 16 4
    # O(logN)
    # nums = [5,9,3,4,1,7]

    if len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False

    mid = len(nums) // 2
    if target == nums[mid]:
        return True
    elif target < nums[mid]:
        nums = nums[:mid]
    else:
        nums = nums[mid:]
    return dac_t(nums, target)


def iter_t(nums, target):
    for i in nums:
        if i == target:
            return True
    return False


if __name__ == "__main__":
    nums = [i for i in range(10000000)]
    r = dac_t(nums, 9999999)
    # r = iter_t(nums, 9999999)
    print(r)

# 对分查找 迭代查找


def dac_t(nums: list[int], target: int, offset: int = 0) -> int:
    # 2 1
    # 4 2
    # 8 3
    # 16 4
    # O(logN)
    # nums = [5,9,3,4,1,7]

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    mid = len(nums) // 2
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        nums = nums[:mid]
    else:
        nums = nums[mid:]
        offset = offset + mid
    return dac_t(nums, target, offset)


def optimize_t(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def iter_t(nums, target):
    for i in nums:
        if i == target:
            return True
    return False


if __name__ == "__main__":
    # nums = [i for i in range(10000000)]
    nums = [-1, 1]
    # r = dac_t(nums, 5546)
    r = optimize_t(nums, 0)
    # r = iter_t(nums, 9999999)
    print(r)

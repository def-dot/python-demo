# 二分查找

def erfen(nums, target, start, end):
    mid = (end - start) // 2 + start
    if nums[mid] == target:
        return mid
    if nums[start] <= target <= nums[mid]:
        return erfen(nums, target, start, mid)
    elif nums[mid] <= target <= nums[end]:
        return erfen(nums, target, mid, end)
    else:
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    index = erfen(nums, -1, 0, len(nums) - 1)
    print(index)

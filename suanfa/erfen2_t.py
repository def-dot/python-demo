# 二分查找，求小于等于某个数的最大数

def erfen(nums, target, start, end):
    if end - start <= 1 and nums[start] <= target <= nums[end]:
        return nums[start]

    mid = (end - start) // 2 + start
    if nums[start] <= target <= nums[mid]:
        return erfen(nums, target, start, mid)
    elif nums[mid] <= target <= nums[end]:
        return erfen(nums, target, mid, end)
    else:
        return -1


if __name__ == '__main__':
    # <=1的最大值 0
    nums = [-1, 0, 3, 5, 9, 12]
    r = erfen(nums, 4, 0, len(nums) - 1)
    print(r)

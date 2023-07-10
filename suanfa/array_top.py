
def force_t(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        return 0 if nums[0] > nums[1] else 1
    else:
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
    if nums[-1] > nums[-2]:
        return len(nums) - 1
    else:
        return 0


def optimize_t(nums: list[int], offset=0) -> int:
    mid = len(nums) // 2
    if nums[mid] < nums[mid+1]:
        nums = nums[mid:]
        return optimize_t(nums, offset=offset+mid)
    elif nums[mid] < nums[mid-1]:
        nums = nums[:mid]
        return optimize_t(nums, offset=mid)
    else:
        return offset+mid


if __name__ == "__main__":
    nums = [1, 4, 2, 7, 8, 3]
    # r = force_t(nums)
    r = optimize_t(nums)
    print(r)


def force_t(nums, n):
    for i in nums:
        for j in i:
            if j == n:
                return True
    return False


def optimize_t(nums: list[int], target: int) -> bool:
    if not nums or not nums[0]:
        return False
    i = len(nums) - 1
    j = 0
    while True:
        if nums[i][j] < target:
            if j == len(nums[0]) - 1:
                return False
            j += 1
        elif nums[i][j] > target:
            if i == 0:
                return False
            i -= 1
        else:
            return True


if __name__ == "__main__":
    nums = [
        [1, 2, 3, 10],
        [5, 6, 9, 13],
        [7, 8, 11, 15]
    ]
    # r = force_t(nums, 10)
    r = optimize_t(nums, 18)
    print(r)

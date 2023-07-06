
def force_t(nums, n):
    for i in nums:
        for j in i:
            if j == n:
                return True
    return False

"""
首先看四个角，左上与右下必定为最小值与最大值，而左下与右上就有规律了：左下元素大于它上方的元素，小于它右方的元素，右上元素与之相反。既然左下角元素有这么一种规律，相当于将要查找的部分分成了一个大区间和小区间，每次与左下角元素比较，我们就知道目标值应该在哪部分中，于是可以利用分治思维来做。

具体做法：

step 1：首先获取矩阵的两个边长，判断特殊情况。
step 2：首先以左下角为起点，若是它小于目标元素，则往右移动去找大的，若是他大于目标元素，则往上移动去找小的。
step 3：若是移动到了矩阵边界也没找到，说明矩阵中不存在目标值。
"""


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
    nums = []
    # r = force_t(nums, 10)
    r = optimize_t(nums, 18)
    print(r)


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


def optimize_t(nums: list[int]) -> int:
    pass


if __name__ == "__main__":
    nums = [1, 4, 2, 7, 8, 3]
    r = force_t(nums)
    print(r)


# [1,2,3,4,5,6,7,8,9]


"""
方法：二分查找（推荐使用）
知识点：分治

分治即“分而治之”，“分”指的是将一个大而复杂的问题划分成多个性质相同但是规模更小的子问题，子问题继续按照这样划分，直到问题可以被轻易解决；“治”指的是将子问题单独进行处理。经过分治后的子问题，需要将解进行合并才能得到原问题的解，因此整个分治过程经常用递归来实现。

思路：

因为题目将数组边界看成最小值，而我们只需要找到其中一个波峰，因此只要不断地往高处走，一定会有波峰。那我们可以每次找一个标杆元素，将数组分成两个区间，每次就较高的一边走，因此也可以用分治来解决，而标杆元素可以选择区间中点。

1
2
3
4
5
6
//右边是往下，不一定有坡峰
if(nums[mid] > nums[mid + 1])
    right = mid;
//右边是往上，一定能找到波峰
else
    left = mid + 1;
具体做法：

step 1：二分查找首先从数组首尾开始，每次取中间值，直到首尾相遇。
step 2：如果中间值的元素大于它右边的元素，说明往右是向下，我们不一定会遇到波峰，但是那就往左收缩区间。
step 3：如果中间值大于右边的元素，说明此时往右是向上，向上一定能有波峰，那我们往右收缩区间。
step 4：最后区间收尾相遇的点一定就是波峰。
"""

